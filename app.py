from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseAlphaGitExp > my-feature-branch says Hello, Docker!'
