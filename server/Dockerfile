FROM python:3.9-alpine

WORKDIR /app

COPY . /app/

RUN apk add --no-cache bash \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && chmod +x entrypoint.sh

# 心跳超时时间（秒）
ENV HEARTBEAT_TIMEOUT 70
# API鉴权秘钥
ENV API_KEY ''
# 服务器名称
ENV SERVER_NAME 'NAS'
# Webhook URL
ENV WEBHOOK_URL 'https://api.day.app/your_token/'

EXPOSE 9000

ENTRYPOINT ["./entrypoint.sh"]
