from flask import Flask, request, jsonify 

import board
import adafruit_dht
import datetime


app =   Flask(__name__)

dht_device = adafruit_dht.DHT22(board.D4)
  
@app.route('/readings', methods = ['GET'])

def readings():
    if(request.method == 'GET'):
        now = datetime.datetime.now()

        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            if temperature is not None and humidity is not None:
                data = {
                    "response": "success",
                    "temperature": '{0:0.1f}'.format(temperature),
                    "humidity": '{0:0.1f}'.format(humidity),
                    "created": now.strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                null_sensor = []
                if temperature is None:
                    null_sensor.append("temperature")
                if humidity is None:
                    null_sensor.append("humidity")
                raise RuntimeError(f"Null sensor values: {', '.join(null_sensor)}")
        except Exception as e:
            data = {
                "response": "error",
                "message": str(e),
                "created": now.strftime("%Y-%m-%d %H:%M:%S")
            }
    return jsonify(data)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
