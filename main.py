
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json

app = Flask(__name__)

# Credenciais do Twilio (substitua com suas credenciais)
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Rota para a página inicial
@app.route("/")
def home():
    return render_template('index.html')

# Rota para salvar dados do formulário do HTML
@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.get_json()
    with open('clientes_investimento.txt', 'a') as file:
        file.write(json.dumps(data) + '\n')
    return {'status': 'success'}, 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)