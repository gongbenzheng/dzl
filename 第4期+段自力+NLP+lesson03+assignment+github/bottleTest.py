# http://localhost:8081/hello/kyle
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8081)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# from bottle import Bottle, run
#
# app = Bottle()
#
# @app.route('/hello')
# def hello():
#     return "Hello World!"
#
# run(app, host='localhost', port=8081)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# from bottle import route, request
#
# @route('/login')
# def login():
#     return '''
#         <form action="/login" method="post">
#             Username: <input name="username" type="text" />
#             Password: <input name="password" type="password" />
#             <input value="Login" type="submit" />
#         </form>
#     '''
#
# @route('/login', method='POST')
# def do_login():
#     username = request.forms.get('username')
#     password = request.forms.get('password')
#     if check_login(username, password):
#         return "<p>Your login information was correct.</p>"
#     else:
#         return "<p>Login failed.</p>"