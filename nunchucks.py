from flask import Flask
from flask import request
from urllib.parse import unquote
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def index():
        data = {
                "email": unquote((request.args.get("email")))
                }
        req_to_nunchucks = requests.post("https://store.nunchucks.htb/api/submit",json=data,verify=False)
        return req_to_nunchucks.text


app.run(host='0.0.0.0', port=80)

