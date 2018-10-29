# from flask import Flask
# import os


# EB looks for an 'application' callable
# application = Flask(__name__)
# application.debug = True

from app import create_app

application = create_app()

# @application.route('/', methods=['GET', 'POST'])
# @application.route('/index', methods=['GET', 'POST'])
# def index():
# 	return 'Hello world!'

if __name__ == '__main__':
	application.run()
# from app import application as app 


# # run the app
# if __name__ == '__main__':
# 	app.debug = True
# 	app.run()
