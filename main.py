from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

MEMORY_FILE = 'robo_memory.json'

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)
@app.route("/")
def home():
    return "Robo Memory API is running"
  
@app.route("/memory", methods=['GET'])
def get_memory():
    memory = load_memory()
    return jsonify(memory)

@app.route("/memory", methods=['POST'])
def update_memory():
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid memory format"}), 400
        save_memory(data)
        return jsonify({"message": "Memory updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
