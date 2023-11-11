FROM alpine:latest

WORKDIR /app

COPY entrypoint.sh /app/entrypoint.sh

RUN apk update && \
    apk add --no-cache bash curl busybox \
    && chmod +x entrypoint.sh

# 默认每分钟执行一次
ENV CRON_EXPRESSION "* * * * *"

ENTRYPOINT ["./entrypoint.sh"]
