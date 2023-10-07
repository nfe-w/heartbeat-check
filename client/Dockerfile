FROM alpine:latest

RUN apk update && apk add --no-cache bash curl busybox

# 默认每分钟执行一次
ENV CRON_EXPRESSION "* * * * *"

RUN echo "$CRON_EXPRESSION /mnt/cron_script.sh" >> /etc/crontabs/root

# 检查文件、赋权、添加任务、启用cron
CMD ["sh", "-c", "\
if [ -e /mnt/cron_script.sh ]; then \
  chmod +x /mnt/cron_script.sh; \
  echo '/mnt/cron_script.sh exists'; \
  crond -f; \
else \
  echo 'Error: /mnt/cron_script.sh file not found.  Please mount the /mnt/cron_script.sh file and try again.'; \
  exit 1; \
fi"]
