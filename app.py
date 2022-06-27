from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseAlphaGitExp > 1.0.1.3 says Hello, Docker!'
