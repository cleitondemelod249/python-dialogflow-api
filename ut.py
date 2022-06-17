import requests
import json
from flask import Flask, request, jsonify

class utils:
    URL = 'https://dialogflow.clients6.google.com/v2/projects/{dialogflow-project}/locations/global/agent/sessions/{sessionid}:detectIntent'
    USERNAME = "your_google_email"
    PASSWD = "your_password"

    def callDialogFlow(headers, payload):
        res = requests.post(utils.URL, headers=headers, json=payload)
        if(res.status_code == 200):
            resp = json.loads(res.text)
            res_message = resp['queryResult']['fulfillmentMessages']
            return jsonify({"message": res_message})
        else:
            return jsonify({"message": "aa"})
