from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.route('/')

def test_server():
    
    # get time
    now = datetime.datetime.now()
    timestring = now.strftime("%Y-%m-%d %H:%M")
    
    # get temperature
    temp = os.popen("vcgencmd measure_temp").readline().replace("temp=", "")
    
    # put together info for templates/index.html
    template_data = {
        'time' : timestring,
        'temp' : temp
    }
    
    return render_template('index.html', **template_data)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')