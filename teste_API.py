from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar os dados do CSV
try:
    df = pd.read_csv(r'C:\\Users\\pirul\\Documents\\Teste\\MySQL\\Operadoras_Plano_Saude\\Relatorio_cadop.csv', delimiter=";", encoding="utf-8")
except Exception as e:
    print(f"Erro ao carregar CSV: {e}")
    df = pd.DataFrame()  # Garante que a variável exista


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if df.empty:
        return jsonify({"error": "Dados não disponíveis"}), 500  # Retorna status 500 (erro interno)
    
    if query:
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
        return jsonify(results.to_dict(orient='records'))
    
    return jsonify({"message": "Nenhum termo de busca fornecido."})

# Rota para a raiz do aplicativo
@app.route('/')
def home():
    return jsonify({"message": "API está rodando. Use /search para buscar dados."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

