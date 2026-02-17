# IMGO Docker 실행 가이드

## 🐳 Docker 환경 구축 및 실행

### 사전 요구사항

```bash
# Docker 설치 확인
docker --version
docker-compose --version

# 예상 출력:
# Docker version 24.0.0 or higher
# Docker Compose version v2.20.0 or higher
```

### 빠른 시작

#### 1. 프로젝트 클론 (이미 완료된 경우 생략)

```bash
git clone https://github.com/almanix00/IMGO.git
cd IMGO
```

#### 2. Docker Compose로 빌드 및 실행

```bash
# 빌드 및 백그라운드 실행
docker-compose up --build -d

# 또는 포그라운드 실행 (로그 확인)
docker-compose up --build
```

#### 3. 브라우저에서 확인

```
http://localhost:8501
```

### 주요 명령어

#### 컨테이너 상태 확인

```bash
docker-compose ps
```

**예상 출력:**
```
NAME        IMAGE          COMMAND                  SERVICE      CREATED         STATUS         PORTS
imgo-demo   imgo-demo      "streamlit run apps/…"   imgo-demo    2 minutes ago   Up 2 minutes   0.0.0.0:8501->8501/tcp
```

#### 로그 확인

```bash
# 실시간 로그 스트리밍
docker-compose logs -f

# 최근 100줄 보기
docker-compose logs --tail=100

# 특정 서비스만
docker-compose logs -f imgo-demo
```

**정상 로그 예시:**
```
imgo-demo  | 
imgo-demo  | Collecting usage statistics...
imgo-demo  | 
imgo-demo  |   You can now view your Streamlit app in your browser.
imgo-demo  | 
imgo-demo  |   URL: http://0.0.0.0:8501
```

#### 컨테이너 중지 및 제거

```bash
# 중지
docker-compose stop

# 중지 및 제거
docker-compose down

# 중지, 제거 및 볼륨 삭제
docker-compose down -v
```

#### 컨테이너 재시작

```bash
# 모든 서비스 재시작
docker-compose restart

# 특정 서비스만
docker-compose restart imgo-demo
```

### Health Check 확인

```bash
# Health check 엔드포인트 테스트
curl http://localhost:8501/_stcore/health

# 예상 출력: HTTP 200 OK
```

또는 브라우저에서:
```
http://localhost:8501/_stcore/health
```

### 문제 해결

#### 1. 포트 8501이 이미 사용 중

```bash
# 포트 사용 프로세스 확인
lsof -i :8501

# 프로세스 종료
kill -9 <PID>

# 또는 docker-compose.yml에서 다른 포트 사용
ports:
  - "8502:8501"  # 호스트:8502 -> 컨테이너:8501
```

#### 2. 컨테이너가 시작되지 않음

```bash
# 상세 로그 확인
docker-compose logs imgo-demo

# 컨테이너 상태 확인
docker-compose ps -a

# 이미지 재빌드 (캐시 무시)
docker-compose build --no-cache
docker-compose up -d
```

#### 3. 데이터 파일이 보이지 않음

```bash
# 볼륨 마운트 확인
docker-compose exec imgo-demo ls -la /app/data/sample

# 예상 출력:
# nist_controls_sample.csv
# mitre_techniques_sample.csv
# ai_rmf_sample.csv
# mapping_sample.csv
# graphrag_paths_sample.json
```

#### 4. Health check 실패

```bash
# 컨테이너 내부 접속
docker-compose exec imgo-demo /bin/bash

# 내부에서 health check 테스트
curl -f http://localhost:8501/_stcore/health

# 로그 확인
cat /var/log/streamlit.log  # (있는 경우)
```

### 고급 사용법

#### 개발 모드 (코드 변경 시 자동 재시작)

`docker-compose.override.yml` 생성:

```yaml
version: '3.8'

services:
  imgo-demo:
    command: streamlit run apps/demo_dashboard.py --server.port=8501 --server.address=0.0.0.0 --server.runOnSave=true
    volumes:
      - ./apps:/app/apps
      - ./data:/app/data
```

실행:
```bash
docker-compose up --build
```

#### 환경 변수 설정

`.env` 파일 생성 (docker-compose가 자동으로 로드):

```bash
APP_TITLE=IMGO Custom Title
APP_VERSION=1.0.0-alpha
ENVIRONMENT=production
```

#### 멀티 스테이지 빌드 (프로덕션)

현재 Dockerfile은 단일 스테이지입니다. 프로덕션 최적화를 원하면:

```dockerfile
# Builder stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["streamlit", "run", "apps/demo_dashboard.py"]
```

### Docker 이미지 정보

#### 이미지 크기 확인

```bash
docker images imgo-demo
```

**예상 크기:** ~500MB (Python 3.12-slim 기반)

#### 이미지 태그 및 푸시 (Docker Hub)

```bash
# 이미지 태그
docker tag imgo-demo:latest almanix00/imgo:1.0.0-alpha
docker tag imgo-demo:latest almanix00/imgo:latest

# Docker Hub 로그인
docker login

# 푸시
docker push almanix00/imgo:1.0.0-alpha
docker push almanix00/imgo:latest
```

### 성능 최적화

#### 메모리 제한 설정

`docker-compose.yml`에 추가:

```yaml
services:
  imgo-demo:
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
```

#### CPU 제한 설정

```yaml
services:
  imgo-demo:
    deploy:
      resources:
        limits:
          cpus: '0.5'
```

### 네트워크 설정

#### 외부 네트워크 연결

```yaml
networks:
  default:
    external: true
    name: shared-network
```

#### 여러 서비스 연결 (예: Nginx 프록시)

```yaml
version: '3.8'

services:
  imgo-demo:
    # ... (기존 설정)
    networks:
      - imgo-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks:
      - imgo-network
    depends_on:
      - imgo-demo

networks:
  imgo-network:
    driver: bridge
```

## 📊 검증 체크리스트

### ✅ Docker 빌드 성공
```bash
docker-compose build
# ✅ Successfully built
# ✅ Successfully tagged imgo-demo:latest
```

### ✅ 컨테이너 실행 성공
```bash
docker-compose up -d
# ✅ Container imgo-demo  Started
```

### ✅ Health Check 통과
```bash
curl http://localhost:8501/_stcore/health
# ✅ HTTP 200 OK
```

### ✅ 데이터 로딩 확인
브라우저에서 http://localhost:8501 접속:
- ✅ Overview 페이지 표시
- ✅ NIST Controls: 9개
- ✅ MITRE Techniques: 10개
- ✅ FKGL 히스토그램 표시
- ✅ 사이드바 Version 정보 표시

### ✅ 모든 페이지 작동 확인
- ✅ Overview
- ✅ NIST Controls
- ✅ MITRE Techniques
- ✅ AI RMF Mapping
- ✅ NIST-MITRE Relationships
- ✅ Knowledge Paths
- ✅ About

## 🐛 알려진 이슈

### 이슈 1: Apple Silicon (M1/M2) Mac에서 빌드 느림
**해결책:**
```bash
# Rosetta 없이 네이티브 빌드
docker-compose build --build-arg BUILDPLATFORM=linux/arm64
```

### 이슈 2: Windows에서 파일 권한 오류
**해결책:**
```bash
# WSL2 사용 권장
# 또는 docker-compose.yml에 추가:
user: "1000:1000"
```

## 📚 추가 자료

- [Docker 공식 문서](https://docs.docker.com/)
- [Docker Compose 레퍼런스](https://docs.docker.com/compose/compose-file/)
- [Streamlit Docker 배포](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)

## 🆘 지원

문제가 발생하면:
1. GitHub Issues: https://github.com/almanix00/IMGO/issues
2. 로그 첨부: `docker-compose logs > logs.txt`
3. 환경 정보: Docker 버전, OS, 오류 메시지
