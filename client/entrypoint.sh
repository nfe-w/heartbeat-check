#!/bin/bash

# 检查任务文件
if [ ! -e /mnt/cron_script.sh ]; then
  echo 'Error: /mnt/cron_script.sh file not found. Please mount the /mnt/cron_script.sh file and try again.'
  exit 1
fi

# 如果/etc/crontabs/root内，存在值包含了"/mnt/cron_script.sh"的行则将其删除
if grep -q "/mnt/cron_script.sh" /etc/crontabs/root; then
  echo 'Crontab already exists. Crontab will be deleted.'
  sed -i "/\/mnt\/cron_script.sh/d" /etc/crontabs/root
fi
# 添加任务
echo 'Add crontab task.'
echo "$CRON_EXPRESSION /mnt/cron_script.sh" >>/etc/crontabs/root
# 赋权
chmod +x /mnt/cron_script.sh
echo '/mnt/cron_script.sh exists. Crontab will be started.'
# 启用cron服务
crond -f
