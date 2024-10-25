
from flask import Flask, request, render_template
import json

app = Flask(__name__)

# Rota para a página inicial
@app.route("/")
def home():
    return render_template('index.html')

# Rota para salvar dados do formulário
@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.get_json()
    with open('clientes_investimento.txt', 'a') as file:
        file.write(json.dumps(data) + '\n')
    return {'status': 'success'}, 200

if __name__ == "__main__":
    app.run(debug=True)
