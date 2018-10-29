from flask import Flask
import os


# EB looks for an 'application' callable
application = Flask(__name__)
application.debug = True

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
	return 'Hello world!' + os.environ.get('TEST_V')



# run the app
if __name__ == '__main__':
	application.run()
