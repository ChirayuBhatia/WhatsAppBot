from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)

# Access token for your app
token = os.environ.get('WHATSAPP_TOKEN')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the request body from the POST
    body = request.json

    # Check the Incoming webhook message
    # print(json.dumps(body, indent=2))

    if 'object' in body:
        if "statuses" in body['entry'][0]['changes'][0]['value']:
            print(body['entry'][0]['changes'][0]['value']['statuses'][0]['status'])
        elif 'messages' in body['entry'][0]['changes'][0]['value']:
            phone_number_id = body['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
            from_number = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
            msg_body = body['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            print(msg_body)
            response = requests.post(
                f'https://graph.facebook.com/v12.0/{phone_number_id}/messages',
                params={'access_token': token},
                json={
                    'messaging_product': 'whatsapp',
                    'to': from_number,
                    'text': {'body': f'Thank You for contacting us'}
                },
                headers={'Content-Type': 'application/json'}
            )
    return '', 200


@app.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = os.environ.get('VERIFY_TOKEN')

    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == verify_token:
            print('WEBHOOK_VERIFIED')
            return challenge, 200
        else:
            return '', 403
    return '', 400


if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 1337), debug=True)
