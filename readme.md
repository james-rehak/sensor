## Description
Simple python server to push temperature and humidity data from a DHT22 Sensor attached to a Raspberry Pie Zero. 
## Configuration
```
sudo apt update
sudo apt install nginx
sudo apt install python3-venv
```
While in sesnor directory containing app
```
python -m venv env
source env/bin/activate
```
While in environment (sensorenv)
```
pip install wheel
pip install gunicorn flask datetime Adafruit_DHT
```
to run:
```
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

Add sensor.service to systemmd here:
```
/etc/systemd/system/sensor.service
```
Enable and start service
```
sudo systemctl start sensor
sudo systemctl enable sensor
```
### Configure Nginx
add sensor nginx config to 
```
/etc/nginx/sites-available/sensor
```
enable serverblock
```
sudo ln -s /etc/nginx/sites-available/sensor /etc/nginx/sites-enabled 
sudo nginx -t
sudo systemctl restart nginx
```

### API Call
`http://{internal_ip}/readings`

Temperature reading in Celsius 

Expected Output:
```
{
    "created": "2023-10-08 15:26:08",
    "humidity": "32.4",
    "response": "success",
    "temperature": "21.6"
}
```
