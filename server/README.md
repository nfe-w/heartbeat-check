```sh
# 构建镜像
docker build -t nfew/heartbeat-check-server-image:latest .

# 启动容器
docker run -d -p 7777:7777 -v ~/config.json:/mnt/config.json --name heartbeat-check-server nfew/heartbeat-check-server-image:latest
```