import app
from app import db
from app.main import bp
from app.models import Schools, GeoData
from flask import render_template, flash, jsonify, request
from sqlalchemy import func



MAPBOX_KEY = app.Config.MAPBOX_KEY


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
	# name = Schools.query.filter_by(id=1).first().chiefname
	# name = Super.query.filter_by(id=7).first().geom
	pt = GeoData.query.get(1)
	name = db.session.scalar(func.ST_AsGeoJSON(pt.geom)) # Получаем координаты в формате JSON
	return render_template('index.html', name=name, title='Moscow')

@bp.route('/')
@bp.route('/hello')
def hello():
	return render_template('hello.html')


@bp.route('/map')
def mapping():
	# return jsonify({'test': 1})
	return render_template('map.html', ACCESS_KEY=MAPBOX_KEY)


@bp.route('/get_gis', methods=['POST'])
def get_gis():
	return jsonify({'text': 'hello world'})
