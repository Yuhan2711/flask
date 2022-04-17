# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,Response
import subprocess
import hello
#from flask_ngrok import run_with_ngrok
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
#run_with_ngrok(app)
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

# ‘/’ URL is bound with hello_world() function.
def hello_world():
    subprocess.call("python hello.py", shell=True)

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(hello.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# main driver function
if __name__ == '__main__':
	app.run(host='127.0.0.1',port=1207)
