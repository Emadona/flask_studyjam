from flask import Flask , redirect , request , url_for , jsonify
import json

app = Flask(__name__ , instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
#app.config.from_envvar('API_SETTINGS')
# localhost:8000/
@app.route('/')
def hello():
    return 'emad'
# localhost:8000/about
@app.route('/about')
def about():
    return 'about page'


# localhost:8000/user/emadona
# @app.route('/user/<username>')
# def user(username):
#     return 'user {}'.format(username)



# localhost:8000/post/0
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post_id {}'.format(post_id)



# localhost:8000/path/config
@app.route('/path/<path:subpath>')
def show_path(subpath):
    return 'path {}'.format(subpath)



# localhost:8000/members?first_name=Emad&last_name=Alharbi
@app.route('/members')
def show_user_profile():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return 'Welcome {} {}'.format(first_name,last_name)

user_admin = 'Emad'



#best practice
# localhost:8000/admin
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'



# localhost:8000/guest/test
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'guest {}'.format(guest)



# localhost:8000/user/name
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest' , guest = name))

@app.route('/algorithm' , methods = ['POST' , 'GET'])
def algorithm():
    if request.method == 'POST':
        return 'You are user POST method'
    else:
        return 'You are user GET method (default http method)'



response = ''

@app.route('/name' , methods = ['GET' , 'POST'])
def nameroute():
    global response

    if (request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data['name']
        response = f'Hi {name} this is Python API'
        return ''
    else:
        return jsonify({'name' : response})


if __name__ == '__main__':
    app.run(port=app.config['PORT'] , debug=app.config['DEBUG'])
