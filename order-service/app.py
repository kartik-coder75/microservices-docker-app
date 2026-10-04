import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Reads the URLs from docker-compose.yml environment variables
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:5000")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:5000")

@app.route("/")
def home():
    return "Order Service (Main Gateway) is Running!"

@app.route("/order")
def process_order():
    # 1. Call User Service
    user_resp = requests.get(f"{USER_SERVICE_URL}/user").json()
    
    # 2. Call Notification Service
    notif_resp = requests.get(f"{NOTIFICATION_SERVICE_URL}/notify").json()
    
    return jsonify({
        "status": "Order Processed",
        "user_info": user_resp,
        "notification": notif_resp
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)