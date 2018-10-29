from flask import render_template
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
	name = 'МИР'
	return render_template('index.html', name=name)
