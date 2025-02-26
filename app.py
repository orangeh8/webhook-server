from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "success", "message": "OK"}), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received alert:")
    print(data)
    return jsonify({"status": "success", "message": "Alert received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)