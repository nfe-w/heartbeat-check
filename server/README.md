```sh
# 构建镜像
docker build -t nfew/heartbeat-check-server:latest .

# 启动容器
docker run -d \
-p 9000:9000 \
-e HEARTBEAT_TIMEOUT=70 \
-e API_KEY='' \
-e SERVER_NAME='服务器' \
-e WEBHOOK_URL='https://api.day.app/your_token/' \
--name heartbeat-check-server \
nfew/heartbeat-check-server:latest
```