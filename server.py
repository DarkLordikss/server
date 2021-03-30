from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    r = request.args.get('dat')
    print('r')
    return render_template('index.html',)

@app.route('/page_1', methods=['GET', 'POST'])
def page_1():
    return 'da'

app.run('0.0.0.0', debug=True)
