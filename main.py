from supabase_service import getContatos
from zapi_service import sendMenssage


def main():
    contatos = getContatos()

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    sendMenssage(contatos)


if __name__ == "__main__":
    main()