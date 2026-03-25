# Controle de Estudos - API


API RESTful desenvolvida para auxiliar estudantes na organização de seus cronogramas de aprendizagem. O sistema permite o gerenciamento de matérias e tópicos com foco em segurança e integridade de dados.

## Tecnologias e Arquitetura

* **Framework:** FastAPI (Python).
* **Banco de Dados:** SQLite com manipulação via SQL puro.
* **Segurança:** Autenticação OAuth2 com Password Flow e Tokens JWT.
* **Identificadores:** Uso de **UUID** para todas as entidades, prevenindo ataques de enumeração (IDOR).
* **Proteção de Dados:** Hashing de senhas utilizando padrões recomendados e mitigação de *Timing Attacks* no fluxo de login através de verificações dummy.

## 🗄️ Modelo de Dados

A API utiliza um modelo relacional estruturado para garantir que cada estudante acesse apenas suas próprias informações:
* **Usuário:** Gerenciamento de credenciais e perfil.
* **Matéria:** Vinculada ao usuário autenticado.
* **Tópico:** Pertencente a uma matéria específica, criando uma hierarquia lógica de estudo.

## 🚀 Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/ArthurFernandes06/Controle_Estudos.git](https://github.com/ArthurFernandes06/Controle_Estudos.git)
   cd Controle_Estudos

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate

3. **Baixe as depêndencias:**
   ```bash
   pip install -r requirements.txt

4. **Inicie o servidor:**
   ```bash
   uvicorn app.main:app --reload

5. **Acesse a documentação Interativa:**
   ```bash
   Abra o navegador em http://127.0.0.1:8000/docs
