from flask import Flask
import getpass
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Deepak S"  
    username = getpass.getuser()

    
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error running top: {str(e)}"

   
    html = f"""
    <p><strong>Name:</strong> {name}</p>
    <p><strong>User:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <p>TOP Output</p>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
