# Desafio b2bflow - Estágio Python

## Setup da tabela no Supabase

Execute os comandos abaixo no SQL Editor do Supabase:

```sql
-- Cria a tabela
create table contatos (
  id bigint generated always as identity primary key,
  nome text not null,
  telefone text not null
);

-- Ativa o RLS (Segurança)
alter table contatos enable row level security;

-- Permite leitura pública utilizando a anon_key
create policy "Permitir leitura publica"
on contatos for select
to anon
using (true);

-- Dados de teste, trocar pelos verdadeiros
insert into contatos (nome, telefone) values
('teste', '5521999999999');
```

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_anon_key

ZAPI_INSTANCE=sua_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Execute o projeto com:

```bash
python main.py
```

O script buscará 3 contatos cadastrados no Supabase e enviará a mensagem personalizada via Z-API no formato:

```text
Olá, <nome_contato> tudo bem com você?
```
