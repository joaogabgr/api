# API - NEFROLOGIA

Um site criado com foco nas mães que possuem filhos com insuficiência renal crônica. Projeto semestral da FATEC DSM 1º SEMESTRE.

## Visão Geral

Aqui as mães poderão compartilhar as histórias de seus filhos e obter mais informações sobre a doença.

## Tecnologias Utilizadas

- HTML
- CSS
- JavaScript
- Python (Flask)
- MySQL

## Requisitos Mínimos

- MySQL Server
- Python
- VirtualEnv

## Funcionalidades Principais

- **Autenticação de Usuário:** Login seguro e autenticação para proteger as contas dos usuários.
- **Persistência de Dados:** Utilização de um banco de dados MySQL para armazenar informações de usuários e postagens.
- **Postagem de Mensagens:** Para que as mães possam compartilhar suas histórias.
- **Sistema de Comentários:** Possibilidade de comentar em postagens e interagir com outros usuários.

## Configuração do Ambiente

Para configurar o ambiente e iniciar o projeto, siga os passos abaixo:

1. Clone este repositório:

```bash
git clone https://github.com/joaogabgr/api .


```bash
git clone https://github.com/joaogabgr/api .
```

2. Ative a maquina virtual:

```bash
py -m venv venv
.\venv\Scripts\activate
```

3. Baixar dependencias:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:

```bash
Altere as informações de usuario no "banco.py" e "models.py"
```

5. Inicar o banco de dados:

```bash
python banco.py
```

6. Iniciar programa:

```bash
python app.py
```

- Projeto feito individualmente por estudo, mas também está sendo desenvolvido em grupo com a utilização do método scrum.
- <a href="https://github.com/Sync-FATEC/API-NEFRO">GitHub do projeto em grupo</a>
