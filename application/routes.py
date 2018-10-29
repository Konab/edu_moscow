from flask import render_template
from application import application as app


@app.route('/')
@app.route('/index')
def index():
	name = 'Константин'
	return render_template('index.html', name=name)
