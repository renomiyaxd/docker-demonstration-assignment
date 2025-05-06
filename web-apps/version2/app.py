from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def os_info():
    return f"Current CPU Count: {os.cpu_count()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
