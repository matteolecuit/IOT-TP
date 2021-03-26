from flask import Flask, jsonify
import serial

app = Flask(__name__)
# initialize Serial
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
ser.flush()


@app.route('/luminosity', methods=['GET'])
def luminosity():
    return raspberry_data()


@app.route('/led', methods=['GET', 'POST'])
def led():
    ser.write(b"toggle\n")
    return jsonify(success=True)


def raspberry_data():
    if ser.in_waiting > 0:
        return ser.readline().decode('utf-8').rstrip()
    return -1


app.run(host='0.0.0.0')
