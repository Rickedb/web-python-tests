from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/another/')
def another_hello_world():
    return 'Another Hello, World!'

@app.route('/hello-for/<int:id>')
def hello_id(id):
    # show the post with the given id, the id is an integer
    return 'Hello for id: %d' % id

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_html(name=None):
    return render_template('hello.html', name=name)
