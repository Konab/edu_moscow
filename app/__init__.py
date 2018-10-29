from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	# with app.app_context():
	db.init_app(app)
	migrate.init_app(app, db)
	bootstrap.init_app(app)

	from app.errors import bp as errors_bp
	app.register_blueprint(errors_bp)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	return app


def test_add_super(sir):
	with app.app_context():
		s = db.Super(sir)
		db.session.add(s)
		db.session.commit


from app import models
