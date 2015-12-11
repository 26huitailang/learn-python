# coding: utf-8

# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
    # return '<h1>Home</h1>'

# @app.route('/signin', methods=['GET'])
# def signin_form():
    # return '''<form action="/signin" method="post">
              # <p><input name="username"></p>
              # <p><input name="password" type="password"></p>
              # <p><button type="submit">Sign In</button></p>
              # </form>'''

# @app.route('/signin', methods=['POST'])
# def signin():
    # # 需要从request对象读取表单内容：
    # if request.form['username']=='admin' and request.form['password']=='Pass2word':
        # return '<h3>Hello, admin!</h3>'
    # return '<h3>Bad username or password.</h3>'

# if __name__ == '__main__':
    # app.run(debug=True)
    
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()