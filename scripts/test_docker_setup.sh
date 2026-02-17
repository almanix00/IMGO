#!/bin/bash

# IMGO Docker 환경 검증 스크립트
# 실행: bash scripts/test_docker_setup.sh

set -e

echo "======================================"
echo "IMGO v1.0.0-alpha Docker 검증 스크립트"
echo "======================================"
echo ""

# 색상 정의
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 체크 함수
check_pass() {
    echo -e "${GREEN}✓${NC} $1"
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
}

check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# 1. Docker 설치 확인
echo "1. Docker 설치 확인..."
if command -v docker &> /dev/null; then
    DOCKER_VERSION=$(docker --version | awk '{print $3}' | sed 's/,//')
    check_pass "Docker installed: $DOCKER_VERSION"
else
    check_fail "Docker not installed"
    echo "   Install from: https://docs.docker.com/get-docker/"
    exit 1
fi

# 2. Docker Compose 확인
echo ""
echo "2. Docker Compose 확인..."
if docker compose version &> /dev/null; then
    COMPOSE_VERSION=$(docker compose version | awk '{print $4}')
    check_pass "Docker Compose installed: $COMPOSE_VERSION"
elif command -v docker-compose &> /dev/null; then
    COMPOSE_VERSION=$(docker-compose --version | awk '{print $4}' | sed 's/,//')
    check_pass "Docker Compose (standalone) installed: $COMPOSE_VERSION"
    check_warn "Consider upgrading to Docker Compose V2 (docker compose)"
else
    check_fail "Docker Compose not installed"
    exit 1
fi

# 3. 필수 파일 확인
echo ""
echo "3. 필수 파일 확인..."
FILES=(
    "Dockerfile"
    "docker-compose.yml"
    "requirements.txt"
    "apps/demo_dashboard.py"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        check_pass "$file exists"
    else
        check_fail "$file missing"
        exit 1
    fi
done

# 4. 데이터 파일 확인
echo ""
echo "4. 샘플 데이터 파일 확인..."
DATA_FILES=(
    "data/sample/nist_controls_sample.csv"
    "data/sample/mitre_techniques_sample.csv"
    "data/sample/ai_rmf_sample.csv"
    "data/sample/mapping_sample.csv"
    "data/sample/graphrag_paths_sample.json"
)

for file in "${DATA_FILES[@]}"; do
    if [ -f "$file" ]; then
        SIZE=$(wc -c < "$file")
        check_pass "$file exists (${SIZE} bytes)"
    else
        check_fail "$file missing"
        exit 1
    fi
done

# 5. Docker 이미지 빌드 테스트
echo ""
echo "5. Docker 이미지 빌드 테스트..."
echo "   (이 단계는 시간이 걸릴 수 있습니다...)"

if docker compose build > /tmp/docker-build.log 2>&1; then
    check_pass "Docker image built successfully"
else
    check_fail "Docker build failed"
    echo "   Check /tmp/docker-build.log for details"
    tail -20 /tmp/docker-build.log
    exit 1
fi

# 6. 이미지 크기 확인
echo ""
echo "6. Docker 이미지 크기 확인..."
IMAGE_NAME=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep -E "imgo|webapp" | head -1)
if [ -n "$IMAGE_NAME" ]; then
    IMAGE_SIZE=$(docker images --format "{{.Size}}" "$IMAGE_NAME")
    check_pass "Image size: $IMAGE_SIZE"
else
    check_warn "Could not determine image size"
fi

# 7. 포트 8501 확인
echo ""
echo "7. 포트 8501 사용 확인..."
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null 2>&1; then
    check_warn "Port 8501 is already in use"
    echo "   Run: docker-compose down (if IMGO is running)"
    echo "   Or: kill -9 \$(lsof -t -i:8501)"
else
    check_pass "Port 8501 is available"
fi

# 8. 컨테이너 시작 테스트
echo ""
echo "8. 컨테이너 시작 테스트..."
echo "   Starting container in detached mode..."

if docker compose up -d > /tmp/docker-up.log 2>&1; then
    check_pass "Container started successfully"
else
    check_fail "Container start failed"
    echo "   Check /tmp/docker-up.log for details"
    tail -20 /tmp/docker-up.log
    exit 1
fi

# 9. Health check 대기
echo ""
echo "9. Health check 대기 (최대 60초)..."
TIMEOUT=60
ELAPSED=0
INTERVAL=5

while [ $ELAPSED -lt $TIMEOUT ]; do
    if curl -sf http://localhost:8501/_stcore/health > /dev/null 2>&1; then
        check_pass "Health check passed (${ELAPSED}s elapsed)"
        break
    else
        echo "   Waiting... (${ELAPSED}s/${TIMEOUT}s)"
        sleep $INTERVAL
        ELAPSED=$((ELAPSED + INTERVAL))
    fi
done

if [ $ELAPSED -ge $TIMEOUT ]; then
    check_fail "Health check timeout"
    echo "   Container logs:"
    docker compose logs --tail=50
    exit 1
fi

# 10. 데이터 로딩 확인
echo ""
echo "10. 데이터 로딩 확인..."
if docker compose exec -T imgo-demo test -f /app/data/sample/nist_controls_sample.csv; then
    check_pass "Data files mounted correctly"
else
    check_fail "Data files not accessible in container"
    exit 1
fi

# 11. 애플리케이션 응답 확인
echo ""
echo "11. 애플리케이션 응답 확인..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8501)
if [ "$HTTP_CODE" = "200" ]; then
    check_pass "Application responding (HTTP $HTTP_CODE)"
else
    check_warn "Unexpected HTTP code: $HTTP_CODE"
fi

# 12. 로그 확인
echo ""
echo "12. 컨테이너 로그 확인..."
if docker compose logs --tail=10 | grep -q "You can now view your Streamlit app"; then
    check_pass "Streamlit started successfully"
else
    check_warn "Streamlit startup message not found (may be normal)"
fi

# 최종 요약
echo ""
echo "======================================"
echo "검증 완료!"
echo "======================================"
echo ""
echo "✓ 모든 필수 검사 통과"
echo ""
echo "다음 단계:"
echo "  1. 브라우저에서 http://localhost:8501 열기"
echo "  2. 다음 항목 확인:"
echo "     - Overview 페이지 표시"
echo "     - NIST Controls: 9개"
echo "     - MITRE Techniques: 10개"
echo "     - FKGL 히스토그램 표시"
echo "     - 사이드바 정보 표시"
echo ""
echo "컨테이너 관리:"
echo "  - 로그 확인: docker compose logs -f"
echo "  - 중지: docker compose stop"
echo "  - 제거: docker compose down"
echo "  - 재시작: docker compose restart"
echo ""
echo "문제가 발생하면 DOCKER_GUIDE.md를 참조하세요."
echo ""
