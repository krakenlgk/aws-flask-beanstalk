from flask import Flask, render_template
from datetime import datetime

# Elastic Beanstalk looks for an 'application' callable by default
application = Flask(__name__)

@application.route('/')
def home():
    deployment_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', deployment_time=deployment_time)

@application.route('/health')
def health():
    return 'OK'

# Run the application
if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0', port=8000)