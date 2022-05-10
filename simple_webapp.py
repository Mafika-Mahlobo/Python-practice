from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'myUniqueKey'

@app.route('/')
def hello()->str:
	return 'Welcome to the simple webapp'

@app.route('/login')
def login()->str:
	session['logged_in'] = True
	return 'You are now logged in'

@app.route('/logout')
def do_logout()->str:
	session.pop('logged_in')
	return 'You are now logged out'

@app.route('/status')
def check_status()->str:
	if not 'logged_in' in session:
		return 'You are NOT logged in'
	else:
		return 'You are logged in'


@app.route('/page1')
def page1()->str:
	return 'this is page one'

@app.route('/page2')
def page2()->str:
	return 'this is page two'


@app.route('/page3')
def page3()->str:
	return 'this is page three'


if __name__ == '__main__':
	app.run(debug=True)