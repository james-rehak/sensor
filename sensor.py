from flask import Flask, request, jsonify 

import Adafruit_DHT
import datetime


app =   Flask(__name__)
  
@app.route('/readings', methods = ['GET'])

def readings():
    if(request.method == 'GET'):
        now = datetime.datetime.now()
        try:
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
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
