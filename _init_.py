from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    env = { 'page_title': 'Main Page' }
    return render_template('layout.html', env=env)

if __name__ == '__main__':
    app.run()
