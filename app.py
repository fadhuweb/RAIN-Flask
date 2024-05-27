from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name", "guest")
    return render_template('index.html', name=name)