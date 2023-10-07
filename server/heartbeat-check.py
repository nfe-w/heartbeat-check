import datetime
import json
import threading
import time

import requests
from flask import Flask, request

app = Flask(__name__)


def custom_print(*args, **kwargs):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{formatted_datetime}] " + " ".join(map(str, args))
    print(message, **kwargs)


with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

# 服务端口
port = config_data.get('port', 7777)
custom_print(f'port->{port}')
# 心跳超时时间（秒）
heartbeat_timeout = config_data.get('heartbeat_timeout', 5)
custom_print(f'heartbeat_timeout->{heartbeat_timeout}')
# API鉴权秘钥
api_key = config_data.get('api_key', None)
custom_print(f'api_key->{api_key}')
# 服务器名称
server_name = config_data.get('server_name', '')
custom_print(f'server_name->{server_name}')
# Webhook URL
webhook_url = config_data.get('webhook_url', None)
custom_print(f'webhook_url->{webhook_url}')

# 上次心跳时间的全局变量
last_heartbeat_time = time.time()
# Event对象用于控制线程的停止
stop_event = threading.Event()
# 默认不检测
stop_event.set()


def do_webhook(msg='无消息明细'):
    try:
        response = requests.get(webhook_url + f'{server_name}/{msg}?level=timeSensitive')
        if response.status_code == 200:
            custom_print("Webhook触发成功")
        else:
            custom_print("Webhook触发失败，状态码: ", response.status_code)
    except Exception as e:
        custom_print("Webhook触发失败:", str(e))


def check_heartbeat():
    global last_heartbeat_time

    while True:
        current_time = time.time()
        time_diff = current_time - last_heartbeat_time

        if not stop_event.is_set() and time_diff > heartbeat_timeout:
            custom_print("心跳断开！触发Webhook...")
            do_webhook('心跳断开，请检查')
            stop_event.set()

        time.sleep(2)


heartbeat_thread = threading.Thread(target=check_heartbeat)
heartbeat_thread.daemon = True
heartbeat_thread.start()


@app.route('/heartbeat')
def heartbeat():
    global last_heartbeat_time

    request_key = request.args.get("api_key")
    if api_key is not None and (request_key is None or request_key != api_key):
        return "Unauthorized", 401

    last_heartbeat_time = time.time()
    if stop_event.is_set():
        do_webhook('已上线')
    stop_event.clear()
    return "Heartbeat OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
