from flask import Flask, render_template, request
import serial, json

app = Flask(__name__)


@app.route('/temperature', methods=['GET'])
def temperature():
    data = raspberry_data()
    return render_template('temperature.html', data=data)


@app.route('/light', methods=['POST'])
def light():
    data = []
    return render_template('light.html', data=data)

def raspberry_data():
 if ser.in_waiting > 0:
  jsonString = ser.readline().decode('utf-8').rstrip()
  try:
   jsonObject = json.loads(jsonString)
   return jsonObject["lumen"]
  except:
   pass
 return -1



app.run(host='localhost', port=5000)
