import os
from dotenv import load_dotenv
import requests

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

headers = {
    "Content-Type": "application/json",
    "Client-Token": os.getenv("ZAPI_CLIENT_TOKEN")
}



def sendMenssage(contatos):
    
    for contato in contatos:
        payload = {
        "phone": contato["telefone"], 
        "message": f"Olá, {contato['nome']} tudo bem com você?"
        }

        try:
            response = requests.post(os.getenv("ZAPI_INSTANCE"), json=payload, headers=headers)
            
            if response.status_code == 200:
                print(f"Mensagem enviada para {contato['nome']}, numero: {contato['telefone']}.")
            else:
                print(f"Erro no envio da menssagem para {contato['nome']}. Status Code: {response.status_code}")
                print("Detalhes do erro:", response.text)

        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro de conexão: {e}")
