from flask import render_template, flash
from app import db
from app.main import bp
# from app.main.forms import PostForm
from app.models import Super


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
	# form = PostForm()
	# if form.validate_on_submit():
	# 	super_u = Super(form.name.data)
	# 	db.session.add(super_u)
	# 	db.session.commit()
	# 	db.session.close()
	# 	flash("It's work!")
	name = 'МИР'
	name = Super.query.filter_by(id=2).first().name
	return render_template('index.html', name=name)
