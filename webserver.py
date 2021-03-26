from flask import Flask, render_template, request, jsonify
import serial
import json

app = Flask(__name__)
# initialize Serial
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
ser.flush()


@app.route('/luminosity', methods=['GET'])
def luminosity():
    data = raspberry_data()
    return jsonify(data)


@app.route('/led', methods=['GET', 'POST'])
def led():
    ser.write(b"toggle\n")
    return jsonify(success=True)


def raspberry_data():
    if ser.in_waiting > 0:
        jsonString = ser.readline().decode('utf-8').rstrip()
        try:
            jsonObject = json.loads(jsonString)
            print(jsonObject["lumen"])
            return jsonObject
        except:
            pass
    return -1


app.run(host='0.0.0.0')
