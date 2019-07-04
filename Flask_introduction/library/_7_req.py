
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/request-info')
def request_info():
    geoip_url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    client_location = requests.get(geoip_url).json()
    return render_template('request/info.html',
                           client_location=client_location)

