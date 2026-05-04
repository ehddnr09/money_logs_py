FROM python:3.11-slim

# 컨테이너 안에서 /app 폴더를 작업 폴더로 사용한다.
# 로컬 폴더가 아니라 Docker 내부 폴더다.
WORKDIR /app

# 로컬의 requirements.txt를 컨테이너의 /app/requirements.txt로 복사한다.
COPY requirements.txt .

# 컨테이너 안에서 패키지를 설치한다.
RUN pip install --no-cache-dir -r requirements.txt

COPY moneylogs ./moneylogs
COPY data ./data

ENTRYPOINT [ "python", "-m", "moneylogs.main" ]
CMD [ "--help" ]