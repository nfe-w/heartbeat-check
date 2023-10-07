FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 7777

# 在容器启动时检查config.json文件的存在，并运行heartbeat-check.py
CMD ["sh", "-c", "\
if [ -f /mnt/config.json ]; then \
    cp -f /mnt/config.json /app/config.json; \
    python heartbeat-check.py; \
else \
    echo 'Error: /mnt/config.json file not found. Please mount the /mnt/config.json file and try again.'; \
    exit 1; \
fi"]
