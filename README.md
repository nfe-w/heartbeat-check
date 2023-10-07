# heartbeat-check

## client（需要检测心跳的服务器）

```shell
# 执行以下命令创建定时脚本, 其中的your_path需要自行指定实际路径，server端ip端口需要替换为实际的ip端口
echo 'curl http://xxx.xxx.xxx.xxx:7777/heartbeat' > /your_path/cron_script.sh
# 启动docker
docker run -d -v /your_path/cron_script.sh:/mnt/cron_script.sh --name heartbeat-check-client nfew/heartbeat-check-client-image:latest
```

## server（最好是有公网ip的服务器）

```shell
# 执行以下命令创建配置文件, 其中的your_path需要自行指定实际路径，your_token需要替换为 Bark app 实际的token，
echo '{
  "heartbeat_timeout": 70,
  "api_key": null,
  "server_name": "NAS",
  "webhook_url": "https://api.day.app/your_token/"
}' > /your_path/config.json
# 启动docker
docker run -d -p 7777:7777 -v /your_path/config.json:/mnt/config.json --name heartbeat-check-server nfew/heartbeat-check-server-image:latest
```