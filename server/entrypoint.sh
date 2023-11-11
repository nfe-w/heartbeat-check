#!/bin/bash

# 生成配置文件
echo "{
  \"heartbeat_timeout\": $HEARTBEAT_TIMEOUT,
  \"api_key\": \"$API_KEY\",
  \"server_name\": \"$SERVER_NAME\",
  \"webhook_url\": \"$WEBHOOK_URL\"
}" >config.json

# 运行heartbeat-check.py
python heartbeat-check.py
