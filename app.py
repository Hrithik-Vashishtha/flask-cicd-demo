from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Flask CI/CD!"

@app.route('/demo')
def demo():
    return "A demo endpoint"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)