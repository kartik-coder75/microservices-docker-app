from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/notify")
def send_notification():
    return jsonify({"status": "Notification sent successfully via Email"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)