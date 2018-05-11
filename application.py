from flask import Flask #imports flash package

application = Flask(__name__) #creates flash app Amazon Elastic Beanstalk will look for an object named "application" in the file "application.py"
application.debug = True # sets debug to true so if there is

@application.route(‘/’, methods=[‘GET’])
def hello():
    return ‘<p>Hello world</p>’

if __name__ == “__main__”:
    application.run()

