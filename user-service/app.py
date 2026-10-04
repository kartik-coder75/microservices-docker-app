from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user")
def get_user():
    return jsonify({"user_id": 101, "name": "Student", "status": "Active"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)