from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    env = { 'page_title': 'Main Page' }
    env['output'] = 'Testing page'
    return render_template('default.html', env=env)

if __name__ == '__main__':
    app.run()
