from flask import Flask, render_template, request, jsonify
import serial
import json

app = Flask(__name__)
# initialize Serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()


@app.route('/temperature', methods=['GET'])
def temperature():
    data = raspberry_data()
    return jsonify(data)


@app.route('/light', methods=['GET', 'POST'])
def light():
    if request.method == 'GET':
        data = {"light": "0"}
        return render_template('light.html', data=data)
    if request.method == 'POST':
        return True


def raspberry_data():
    if ser.in_waiting > 0:
        jsonString = ser.readline().decode('utf-8').rstrip()
        try:
            jsonObject = json.loads(jsonString)
            print(jsonObject["lumen"])
            return jsonObject["lumen"]
        except:
            pass
    return -1


app.run(host='localhost', port=5000)
