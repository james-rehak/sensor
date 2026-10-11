from flask import Flask, request, jsonify 

import board
import adafruit_dht
import datetime


app =   Flask(__name__)

dht_device = adafruit_dht.DHT22(board.D4)
  
@app.route('/readings', methods = ['GET'])
def readings():
    now = datetime.datetime.now()
    temperature = None
    humidity = None

    for attempt in range(3):
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            if temperature is not None and humidity is not None:
                break  # Got Readings
        except Exception:
            pass

        # Try 2 more times with 2 second pause
        if attempt < 2:
            time.sleep(2.0)

    try:
        missing = []
        if temperature is None:
            missing.append("temperature")
        if humidity is None:
            missing.append("humidity")

        if missing:
            raise RuntimeError(f"Null sensor values: {', '.join(missing)}")

        data = {
            "response": "success",
            "temperature": '{0:0.1f}'.format(temperature),
            "humidity": '{0:0.1f}'.format(humidity),
            "created": now.strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        data = {
            "response": "error",
            "message": str(e),
            "created": now.strftime("%Y-%m-%d %H:%M:%S")
        }
    return jsonify(data)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
