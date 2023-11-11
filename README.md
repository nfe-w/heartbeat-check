# heartbeat-check

## client（需要检测心跳的服务器）

```shell
# 执行以下命令创建定时脚本, 其中的your_path需要自行指定实际路径，server端ip端口需要替换为实际的ip端口
echo 'curl http://xxx.xxx.xxx.xxx:9000/heartbeat' > /your_path/cron_script.sh
# 启动docker
docker run -d -v /your_path/cron_script.sh:/mnt/cron_script.sh --name heartbeat-check-client nfew/heartbeat-check-client:latest
```

## server（最好是有公网ip的服务器，或者容器镜像云函数）

```shell
# 启动docker，your_token需要替换为 Bark app 实际的token
docker run -d \
-p 9000:9000 \
-e WEBHOOK_URL='https://api.day.app/your_token/' \
--name heartbeat-check-server \
nfew/heartbeat-check-server:latest
```