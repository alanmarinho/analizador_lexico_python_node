from flask import Flask, render_template, request, jsonify
from backend.analizador import analisador_lexico
app = Flask(__name__)

app = Flask(__name__, static_folder='frontend', static_url_path='/frontend')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/analizador', methods=['GET'])
def get_analise():
    espressao = request.args.get('input')
    if espressao is None:
        return jsonify({"error": "Expressão não fornecida"}), 400
    tokens = analisador_lexico(espressao)
    return jsonify(tokens)
if __name__ == "__main__":
    app.run(debug=True)