from flask import Flask


# EB looks for an 'application' callable
application = Flask(__name__)
application.debug = True

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
	return 'hello!'



# run the app
if __name__ == '__main__':
	application.run()
