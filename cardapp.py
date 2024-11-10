from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return '<h1>TEST</h1>'
app.run()