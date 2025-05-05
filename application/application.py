from flask import Flask, render_template

# Elastic Beanstalk looks for an 'application' callable by default
application = Flask(__name__)

@application.route('/')
def home():
    return '<h1>Hello, World!</h1><p>This is a Flask app deployed on AWS Elastic Beanstalk.</p>'

@application.route('/health')
def health():
    return 'OK'

# Run the application
if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0', port=8000)