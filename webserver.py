from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/temperature', methods=['GET'])
def temperature():
    data = []
    return render_template('temperature.html', data=data)


@app.route('/light', methods=['POST'])
def light():
    data = []
    return render_template('light.html', data=data)


app.run(host='localhost', port=5000)
