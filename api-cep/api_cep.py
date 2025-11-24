from flask import Flask, jsonify
import requests

app = Flask(__name__)

def consultar_cep(cep):
    cep = cep.replace("-", "").strip()
    url = f"http://viacep.com.br/ws/{cep}/json"
    reposta = requests.get(url)
    dados = reposta.json()

    if "erro" in dados:
        return None
    return{
        "logradouro": dados.get("logradouro"),
        "bairro": dados.get("bairro"),
        "cidade": dados.get("localidade"),
        "estado": dados.get("uf")
    }

@app.route("/cep/<cep>")
def api_cep(cep):
    resultado = consultar_cep(cep)
    if resultado:
        return jsonify(resultado)
    else:
        return jsonify({"erro": "CEP invalido"}), 400


@app.route("/cep/<cep>/formatado")
def cep_formatado(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return jsonify({"erro": "Não foi possível consultar o CEP"}), 400

    dados = resposta.json()

    if "erro" in dados:
        return jsonify({"erro": "CEP inválido"}), 400

    # Formatando dados
    endereco = {
        "CEP": dados["cep"],
        "Rua": dados["logradouro"],
        "Bairro": dados["bairro"],
        "Cidade": dados["localidade"],
        "Estado": dados["uf"]
    }

    return jsonify(endereco)
if __name__=="__main__":
    app.run(debug=True)
