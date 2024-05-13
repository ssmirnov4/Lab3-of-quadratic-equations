from flask import Flask, render_template, request
import equation

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = int(request.form.get('c'))
    return render_template('index.html', ans=equation.discriminant(a, b, c))


if __name__ == '__main__':
    app.run()