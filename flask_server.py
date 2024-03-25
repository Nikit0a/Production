from flask import Flask, render_template, abort
import os
import subprocess
from subprocess import Popen

app = Flask(__name__, template_folder='templates')

# path to LED scripts
LED_SCRIPTS_PATH = "led_patterns/"

# List of supported emotions
emotions = ['happy', 'sad', 'excited', 'calm', 'angry', 'nervous', 'fearful', 'love']

# dictionary for tracking the current process
current_process = None

def run_led_script_async(script_name):
    global current_process
    try:
        if current_process:
            # Trying to interrupt the current process if it exists
            current_process.terminate()
            current_process.wait(timeout=1)  # We give the process time to complete
    except subprocess.TimeoutExpired:
        print(f"Process {script_name} didn't finish on time.")
    except Exception as e:
        print(f"Error at the end of the process: {e}")
    finally:
        script_path = os.path.join(LED_SCRIPTS_PATH, script_name)
        # Starting a new process
        try:
            current_process = Popen(["python3", script_path])
        except Exception as e:
            print(f"Error when running the script {script_name}: {e}")


        
@app.route('/')
def home():
    # We run the script to turn off the light when returning to the main page
    run_led_script_async("lights_out.py")
    return render_template("html_melodic.html")

 
@app.route('/<emotion>')
   # Dynamic route based on emotion. This function responds to URLs like '/happy', '/sad', etc
    # It renders a corresponding HTML template if the emotion is in the predefined list
def emotion_page(emotion):
    if emotion in emotions:
        run_led_script_async(f"{emotion}.py")
        return render_template(f'{emotion}.html')
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    # Returning a custom template 404.html if the error is 404
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    # Server error, if the error is 500
    return render_template('500.html'), 500



if __name__ == '__main__':
    # Running the app with the host set to '0.0.0.0' makes it accessible on the local network
    # Debug mode is turned on for development purposes
    app.run(host='0.0.0.0', port=5000, debug=True)
