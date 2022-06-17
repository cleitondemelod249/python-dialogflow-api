from flask import Flask, request, jsonify
from google_auth_oauthlib.flow import Flow
from ut import utils
import json

class values:
    token = ""

app = Flask(__name__)
appflow = Flow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['openid', 'https://www.googleapis.com/auth/dialogflow',
            'https://www.googleapis.com/auth/cloud-platform'],
    redirect_uri='http://localhost:5000')

@app.route('/', methods=['GET'])
def query_example():
    code = request.args.get('code')
    appflow.fetch_token(code=code)
    credentials = appflow.credentials
    values.token = credentials.token
    return jsonify({"token": values.token})

@app.route('/v1/message/', methods=['POST'])
def query_example2():
    dt = request.data
    txt = json.loads(dt)
    payload = {
        "queryParams": {
            "source": "DIALOGFLOW_CONSOLE",
            "timeZone": "America/Sao_Paulo",
            "sentimentAnalysisRequestConfig": {
                "analyzeQueryTextSentiment": True
            }
        },
        "queryInput": {
            "text": {"text": txt.get('msg'), "languageCode": "pt-br"}
        }
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Bearer ' + values.token,
        'content-type': 'application/json; charset=UTF-8',
    }
    return utils.callDialogFlow(headers, payload)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
