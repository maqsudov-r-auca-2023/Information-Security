from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='.')

CORS(app)

data_file = "login_attempts.txt"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username and password:
        return jsonify({"message": "⚠️ Warning: This is a phishing simulation!"}), 200
    else:
        return jsonify({"message": "Invalid input"}), 400

if __name__ == "__main__":
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            pass
    app.run(debug=True, port=8000)

