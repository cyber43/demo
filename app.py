from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "this is demo. sixth"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
