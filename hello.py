from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
	return "admin page"

@app.route('/guest')
def guest():
	return "guest page"

@app.route('/user/<name>')
def user(name):
	if name=='admin':
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('guest', guest = name))


if __name__ == '__main__':
	app.run(debug = True)
