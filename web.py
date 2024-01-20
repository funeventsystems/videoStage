
from fileinput import filename 
from flask import * 
import os
import time
import json
import subprocess

app = Flask(__name__)




os.system("./home/pi/screensaver.sh")
# Setup, clears the screen and makes it so no system messages show.
@app.route('/setup/', methods=['GET','POST'])
def setup():
    os.system("fbi --autozoom --fitwidth -T 1 --noverbose --device /dev/fb0 /home/pi/marbles.jpg")
    initialized = "yes"
    image = "splash"
    return("Setup")
# Displays a cat previously saved in memory.
@app.route('/cat/', methods=['GET', 'POST'])
def cat():
    image = "cat"
    os.system("cat /home/pi/cat.fb > /dev/fb0")
    return "Cat!"
# Displays a fish, saved in memory
@app.route('/fish/', methods=['GET', 'POST'])
def fish():
    image = "fish"
    os.system("cat /home/pi/fish.fb > /dev/fb0")
    return "Fish"
#Displays random noise, to test the processor.
@app.route('/random/', methods=['GET', 'POST'])
def random():
    image = "randomNoise"
    os.system("cat /dev/urandom > /dev/fb0")
    return "Random"

# Route to list current image
@app.route('/status/image/', methods=['GET', 'POST'])
def imageStatus():
    return image
# Route to list current initialization
@app.route('/status/initialized/', methods=['GET', 'POST'])
def initializedStatus():
    return initialized
#Route to run a command on the system.
@app.route('/command/', methods=['POST', 'FETCH'])
def command():
    data = request.get_json()
    receivedCommand = data
    os.system(receivedCommand["sentCommand"])
    return "Command worked, possibly. Look at the screen!"
#File upload
@app.route('/upload', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)   
        return render_template("Acknowledgement.html", name = f.filename)   
# upload page
@app.route('/uploadpage')   
def main():   
    return render_template("upload.html")    
#Main page.
@app.route("/") 
def hello(): 
    message = "Hello, World"
    return render_template('index.html',  
                           message=message) 
def splash():
    image = splash
    os.system("cat /home/pi/dog.fb > /dev/fb0")



# Scene routes to start a numberical scene.
@app.route('/startScene/<scene_id>')
def start_scene(scene_id):
    # Validate and sanitize the scene_id to prevent command injection
    if not scene_id.isdigit():
        return 'Invalid scene_id'

    # Use subprocess.run to execute the command safely
    command = f"cat /home/pi/{scene_id}.fb > /dev/fb0"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.returncode == 0:
        return f'Starting scene {scene_id}'
    else:
        return f'Error starting scene {scene_id}: {result.stderr}'

if __name__ == '__main__':
    app.run(debug=True)






if __name__ == '__main__':
    splash()
    app.run(host='0.0.0.0', port=105)
    

