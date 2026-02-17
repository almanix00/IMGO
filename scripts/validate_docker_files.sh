#!/bin/bash

# IMGO Docker 설정 검증 스크립트 (Docker 없이)
# 실행: bash scripts/validate_docker_files.sh

echo "======================================"
echo "IMGO Docker 설정 파일 검증"
echo "======================================"
echo ""

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_pass() { echo -e "${GREEN}✓${NC} $1"; }
check_fail() { echo -e "${RED}✗${NC} $1"; }
check_warn() { echo -e "${YELLOW}⚠${NC} $1"; }

ERRORS=0

# 1. Dockerfile 검증
echo "1. Dockerfile 검증..."
if [ -f "Dockerfile" ]; then
    check_pass "Dockerfile exists"
    
    # Python 버전 확인
    if grep -q "python:3.12" Dockerfile; then
        check_pass "Python 3.12 base image"
    else
        check_fail "Python 3.12 not specified"
        ERRORS=$((ERRORS + 1))
    fi
    
    # WORKDIR 확인
    if grep -q "WORKDIR /app" Dockerfile; then
        check_pass "WORKDIR set to /app"
    else
        check_warn "WORKDIR not standard"
    fi
    
    # Port 확인
    if grep -q "EXPOSE 8501" Dockerfile; then
        check_pass "Port 8501 exposed"
    else
        check_fail "Port 8501 not exposed"
        ERRORS=$((ERRORS + 1))
    fi
    
    # CMD 확인
    if grep -q 'CMD.*streamlit.*run.*apps/demo_dashboard.py' Dockerfile; then
        check_pass "Streamlit CMD configured"
    else
        check_fail "Streamlit CMD not found"
        ERRORS=$((ERRORS + 1))
    fi
else
    check_fail "Dockerfile not found"
    ERRORS=$((ERRORS + 1))
fi

# 2. docker-compose.yml 검증
echo ""
echo "2. docker-compose.yml 검증..."
if [ -f "docker-compose.yml" ]; then
    check_pass "docker-compose.yml exists"
    
    # 서비스 이름 확인
    if grep -q "imgo-demo:" docker-compose.yml; then
        check_pass "Service 'imgo-demo' defined"
    else
        check_warn "Service name not standard"
    fi
    
    # 포트 매핑 확인
    if grep -q '"8501:8501"' docker-compose.yml; then
        check_pass "Port mapping 8501:8501"
    else
        check_fail "Port mapping not configured"
        ERRORS=$((ERRORS + 1))
    fi
    
    # 볼륨 마운트 확인
    if grep -q "./data:/app/data" docker-compose.yml; then
        check_pass "Data volume mounted"
    else
        check_warn "Data volume not mounted (may cause issues)"
    fi
    
    # Health check 확인
    if grep -q "healthcheck:" docker-compose.yml; then
        check_pass "Health check configured"
    else
        check_warn "Health check not configured"
    fi
else
    check_fail "docker-compose.yml not found"
    ERRORS=$((ERRORS + 1))
fi

# 3. requirements.txt 검증
echo ""
echo "3. requirements.txt 검증..."
if [ -f "requirements.txt" ]; then
    check_pass "requirements.txt exists"
    
    REQUIRED_PACKAGES=("streamlit" "pandas" "plotly" "numpy")
    for pkg in "${REQUIRED_PACKAGES[@]}"; do
        if grep -qi "^$pkg" requirements.txt; then
            check_pass "Package $pkg listed"
        else
            check_fail "Package $pkg missing"
            ERRORS=$((ERRORS + 1))
        fi
    done
else
    check_fail "requirements.txt not found"
    ERRORS=$((ERRORS + 1))
fi

# 4. 애플리케이션 파일 확인
echo ""
echo "4. 애플리케이션 파일 확인..."
APP_FILES=(
    "apps/demo_dashboard.py"
)

for file in "${APP_FILES[@]}"; do
    if [ -f "$file" ]; then
        SIZE=$(wc -c < "$file")
        check_pass "$file exists (${SIZE} bytes)"
    else
        check_fail "$file missing"
        ERRORS=$((ERRORS + 1))
    fi
done

# 5. 데이터 파일 확인
echo ""
echo "5. 샘플 데이터 파일 확인..."
DATA_FILES=(
    "data/sample/nist_controls_sample.csv"
    "data/sample/mitre_techniques_sample.csv"
    "data/sample/ai_rmf_sample.csv"
    "data/sample/mapping_sample.csv"
    "data/sample/graphrag_paths_sample.json"
)

MISSING_DATA=0
for file in "${DATA_FILES[@]}"; do
    if [ -f "$file" ]; then
        LINES=$(wc -l < "$file" 2>/dev/null || echo "N/A")
        SIZE=$(wc -c < "$file")
        check_pass "$file exists (${SIZE} bytes, ${LINES} lines)"
    else
        check_fail "$file missing"
        ERRORS=$((ERRORS + 1))
        MISSING_DATA=$((MISSING_DATA + 1))
    fi
done

# 6. Python 코드 구문 검사
echo ""
echo "6. Python 코드 검증..."
if command -v python3 &> /dev/null; then
    if python3 -m py_compile apps/demo_dashboard.py 2>/dev/null; then
        check_pass "Python syntax valid"
    else
        check_fail "Python syntax errors"
        ERRORS=$((ERRORS + 1))
    fi
else
    check_warn "Python3 not available for validation"
fi

# 7. 디렉토리 구조 확인
echo ""
echo "7. 디렉토리 구조 확인..."
REQUIRED_DIRS=("apps" "data/sample" "docs" "scripts")

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        COUNT=$(find "$dir" -type f | wc -l)
        check_pass "$dir exists (${COUNT} files)"
    else
        check_fail "$dir missing"
        ERRORS=$((ERRORS + 1))
    fi
done

# 8. .dockerignore 확인 (선택적)
echo ""
echo "8. .dockerignore 확인 (선택적)..."
if [ -f ".dockerignore" ]; then
    check_pass ".dockerignore exists"
else
    check_warn ".dockerignore not found (not critical but recommended)"
    echo "   Consider creating .dockerignore with:"
    echo "   __pycache__"
    echo "   *.pyc"
    echo "   .git"
    echo "   .env"
fi

# 최종 요약
echo ""
echo "======================================"
echo "검증 결과"
echo "======================================"
echo ""

if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✓ 모든 필수 검사 통과${NC}"
    echo ""
    echo "Docker 환경이 올바르게 구성되었습니다."
    echo ""
    echo "다음 단계:"
    echo "  1. Docker 설치 확인: docker --version"
    echo "  2. 이미지 빌드: docker-compose build"
    echo "  3. 컨테이너 실행: docker-compose up -d"
    echo "  4. 브라우저 접속: http://localhost:8501"
    echo ""
    echo "자세한 사용법은 DOCKER_GUIDE.md를 참조하세요."
    exit 0
else
    echo -e "${RED}✗ ${ERRORS}개의 오류 발견${NC}"
    echo ""
    echo "다음 항목을 수정한 후 다시 실행하세요."
    exit 1
fi
