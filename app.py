from flask import Flask, jsonify
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Get the system username
    username = os.getlogin()

    # Get the current server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

    # Get the top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> A Suhail Ahmed</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """
    return response

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
