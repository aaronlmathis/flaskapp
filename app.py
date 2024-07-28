from flask import Flask
import platform

application = Flask(__name__)

@application.route("/")


def index():
	return "Nobody expects the spanish inquisition!"

@application.route("/python-version")
def python_version():
	python_version = platform.python_version()
	return f'The python version running on this host is: {python_version}'

if __name__ == "__main__":
	application.run(host='0.0.0.0', port='8080')


