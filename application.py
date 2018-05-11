from flask import Flask #imports flash package

application = Flask(__name__) #creates flash app Amazon Elastic Beanstalk will look for an object named "application" in the file "application.py"
application.debug = True # sets debug to true so if there is an error, it will display in the browser. This is a flaw for production as it shows how app works

@application.route(‘/’, methods=[‘GET’]) #flask decorator. If use goes to the "/" URL of your website (homepage) then run lines 7-8
def hello(): #function named hello It will return the text "Hello World"
    return ‘<p>Hello world</p>’

if __name__ == “__main__”: #Initialise the Flask Application
    application.run()

