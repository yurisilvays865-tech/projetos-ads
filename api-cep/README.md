📄 README — API de Consulta de CEP (Flask)
📌 Descrição

Esta é uma API simples desenvolvida em Python + Flask que consulta dados de endereço a partir de um CEP utilizando a API pública ViaCEP.
O objetivo do projeto é praticar conceitos de criação de APIs REST, rotas, requisições HTTP e integração com serviços externos.

🚀 Tecnologias utilizadas

Python 3

Flask

Requests

ViaCEP (API pública)

📂 Estrutura do Projeto
/api-cep
│── app.py
│── requirements.txt
└── README.md

▶️ Como executar o projeto
1. Instalar dependências
pip install -r requirements.txt

2. Executar o servidor Flask
python app.py


O servidor rodará por padrão em:

http://127.0.0.1:5000

🔎 Como usar a API
Endpoint principal:
GET /cep/<cep>

Exemplo:
http://127.0.0.1:5000/cep/01001000

Retorno esperado:
{
  "bairro": "Sé",
  "cep": "01001-000",
  "complemento": "lado ímpar",
  "ddd": "11",
  "gia": "1004",
  "ibge": "3550308",
  "localidade": "São Paulo",
  "logradouro": "Praça da Sé",
  "siafi": "7107",
  "uf": "SP"
}

❗ Erros possíveis

Se o CEP não existir:

{
  "erro": "CEP não encontrado"
}


Se faltar o parâmetro ou CEP inválido:

{
  "erro": "CEP inválido"
}

📚 Aprendizados do projeto

Como criar rotas Flask

Como integrar APIs externas (ViaCEP)

Como usar jsonify para retornar respostas JSON

Como organizar um pequeno projeto backend