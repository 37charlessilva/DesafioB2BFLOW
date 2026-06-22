import os
from dotenv import load_dotenv
from supabase import create_client

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

# Inicializa o cliente do Supabase

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


def getContatos(limit=3):
    try:
        """Retorna um lista com 3 contatos"""
        response = (
            supabase
            .table("contatos")
            .select("*")
            .limit(limit)
            .execute()
        )

        
        return response.data
    
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []
