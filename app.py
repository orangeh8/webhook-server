# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({"status": "success", "message": "OK"}), 200
#
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.get_json()
#     print("Received alert:")
#     print(data)
#     return jsonify({"status": "success", "message": "Alert received"}), 200
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)


from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "webhook_data.log"  # 数据保存的文件

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "success", "message": "OK"}), 200

# Webhook 接收端点
@app.route('/webhook', methods=['POST'])
def receive_webhook():
    # 获取 webhook 数据
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"status": "error", "message": "No JSON data received"}), 400

    # 添加时间戳，便于记录
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"timestamp": timestamp, "data": data}

    # 写入文件
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    # 返回成功响应
    return jsonify({"status": "success", "message": "Webhook received"}), 200

# API 读取 webhook 数据
@app.route('/webhook/data', methods=['GET'])
def get_webhook_data():
    try:
        # 读取文件中的所有记录
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 将每行解析为 JSON 对象
        data = [json.loads(line.strip()) for line in lines if line.strip()]
        return jsonify({"status": "success", "data": data}), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "No data found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)