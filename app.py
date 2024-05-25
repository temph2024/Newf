import subprocess
from flask import Flask
import time
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Joneswarrior. Bitch bakchodi nhi samajh me aaya kya. Sabki maa ki chut.'

if __name__ == "__main__":
    # Run the additional scripts
    subprocess.Popen(['python3', 'scrape.py'])
    time.sleep(40)
    subprocess.Popen(['python3', 'getviews.py'])
    
    # Start the Flask app
    app.run()
