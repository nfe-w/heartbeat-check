```sh
# 构建镜像
docker build -t nfew/heartbeat-check-client:latest .

# 启动容器
docker run -d -v ~/cron_script.sh:/mnt/cron_script.sh --name heartbeat-check-client nfew/heartbeat-check-client:latest
```