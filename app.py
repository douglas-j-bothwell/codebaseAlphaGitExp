from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseAlphaGitExp > 1.0.1.2 says Hello, Docker!'
