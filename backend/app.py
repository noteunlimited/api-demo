from host import API_URL, USER_API_KEY, API_URL,USER_API_EMAIL, USER_API_KEY_NAME
from flask import Flask, json,jsonify
from flask_cors import CORS
from requests import get
import os


app = Flask(__name__)
CORS(app)


global ACCESS_TOKEN
ACCESS_TOKEN = None

@app.route("/get_access_token", methods=["GET"])
def get_access_token() -> str:
    global ACCESS_TOKEN
    if ACCESS_TOKEN is None:
        headers = {
            'X-API-Key': USER_API_KEY
            }
        result = get(f"{API_URL}access-token/{USER_API_EMAIL}/{USER_API_KEY_NAME}",headers = headers,verify=False)
        res_json = result.json()
        if result.status_code == 200:
            ACCESS_TOKEN = res_json
            return ACCESS_TOKEN
        else:
            return res_json
    else:
        return ACCESS_TOKEN


@app.route("/get_notes", methods=["GET"])
def get_notes() -> list:
    filename = os.path.join(app.static_folder, 'data', 'notes.json')
    with open(filename) as test_file:
        data = json.load(test_file)
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
