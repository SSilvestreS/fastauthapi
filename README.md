# FastAuthAPI

![FastAuthAPI Banner](https://via.placeholder.com/1200x400.png?text=FastAuthAPI)

[![Status](https://img.shields.io/badge/Status-Completo-green)](https://github.com/SSilvestreS/NexusPM)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

##  Visão Geral

**FastAuthAPI** é uma API RESTful moderna construída com **FastAPI**, projetada para oferecer autenticação segura via JWT, gerenciamento de usuários e integração eficiente com banco de dados através do SQLAlchemy. Este projeto foi desenvolvido com foco em **segurança, escalabilidade e boas práticas de desenvolvimento**, servindo como uma base robusta para aplicações web e mobile.

##  Tecnologias Utilizadas

* **Python 3.8+**
* **FastAPI** - Framework web de alta performance
* **SQLAlchemy** - ORM para banco de dados
* **SQLite** (configurável para outros bancos) - Banco de dados relacional
* **JWT (JSON Web Tokens)** - Autenticação segura
* **bcrypt** - Hashing de senhas
* **Uvicorn** - Servidor ASGI para execução

##  Instalação

Clone o repositório:

```bash
git clone https://github.com/Zepphyrum/fastauthapi.git
cd fastauthapi
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

##  Configuração

Renomeie `.env.example` para `.env` e configure as variáveis de ambiente:

```env
DATABASE_URL=sqlite:///./database.db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

##  Rodando a Aplicação

Inicie o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa em:

```
http://127.0.0.1:8000/docs
```

##  Funcionalidades

* **Cadastro de Usuário:** Registro seguro com validação e hashing de senha.
* **Login de Usuário:** Geração e validação de tokens JWT.
* **Gerenciamento de Usuários:** Endpoints para visualização e atualização de dados.
* **Segurança:** Senhas protegidas e endpoints autenticados.
* **Documentação Interativa:** Swagger UI e ReDoc para testes e exploração da API.

##  Testes

Execute testes automatizados para validar funcionalidades:

```bash
pytest
```

![Tests](https://img.shields.io/badge/tests-passed-brightgreen)

##  Boas Práticas

* Arquitetura modular para fácil manutenção.
* Padrões de segurança recomendados para APIs.
* Documentação clara e interativa via FastAPI.
* Preparado para deployment em ambientes de produção.

##  Contribuições

Contribuições são bem-vindas! Siga os passos:

1. Fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit das alterações (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

##  Contato

* E-mail: [sauloxl31@gmail.com](mailto:sauloxl31@gmail.com)
* LinkedIn: [Saulo Silvestre](https://www.linkedin.com/in/saulo-silvestre-042b632b8)


