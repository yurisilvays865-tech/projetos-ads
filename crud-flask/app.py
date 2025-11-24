from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Base de dados em memória (só para teste)
usuarios = []

# HTML simples para listar e cadastrar
template = """
<!doctype html>
<html>
<head>
    <title>CRUD com Flask</title>
</head>
<body>
    <h1>Cadastro de Usuários</h1>
    <form method="post" action="/adicionar">
        Nome: <input type="text" name="nome" required>
        <input type="submit" value="Adicionar">
    </form>

    <h2>Usuários Cadastrados</h2>
    <ul>
        {% for usuario in usuarios %}
            {% set i = loop.index0 %}
            <li>
                {{ usuario }}
                <a href="{{ url_for('editar', indice=i) }}">Editar</a> |
                <a href="{{ url_for('excluir', indice=i) }}">Excluir</a>
            </li>
        {% endfor %}
    </ul>

    <a href="/">Voltar</a>
</body>
</html>
"""

# Página inicial - lista usuários
@app.route("/")
def index():
    return render_template_string(template, usuarios=usuarios)

# Adicionar novo usuário
@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    usuarios.append(nome)
    return redirect(url_for("index"))

# Editar usuário
@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):
    if request.method == "POST":
        novo_nome = request.form["nome"]
        usuarios[indice] = novo_nome
        return redirect(url_for("index"))
    return render_template_string("""
        <h1>Editar Usuário</h1>
        <form method="post">
            Novo nome: <input type="text" name="nome" value="{{ usuarios[indice] }}" required>
            <input type="submit" value="Salvar">
        </form>
    """, usuarios=usuarios, indice=indice)

# Excluir usuário
@app.route("/excluir/<int:indice>")
def excluir(indice):
    usuarios.pop(indice)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
