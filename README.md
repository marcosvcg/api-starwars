# Processo Seletivo - PowerOfData | Caste Técnico: Avaliação para Cargo de Desenvolvedor Back End Python

API desenvolvida em **Python** utilizando **FastAPI**, que atua como uma camada intermediária para consumo da **SWAPI (Star Wars API)**. O objetivo do projeto é expor endpoints organizados, relacionais e testados, permitindo com que o usuário consulte diferentes informações baseadas nos dados da API do Star Wars de forma facilitada.

---

## 🚀 Funcionalidades

* Consulta aos recursos da SWAPI:

  * People
  * Films
  * Starships
  * Vehicles
  * Species
  * Planets
* Paginação e busca de recursos pelo nome/título/modelo
* Consulta individual por ID
* Navegação relacional entre recursos (ex.: filmes de um personagem)
* Testes automatizados com `pytest`
* Documentação do SwaggerUI

---

## 🗂️ Estrutura do Projeto

```text
├── 📁 api
│   ├── 🐍 base.py        # Classes base (Model e QuerySet)
│   ├── 🐍 resources.py   # Modelagem dos recursos da SWAPI
│   ├── 🐍 router.py      # Definição dos endpoints
│   └── 🐍 utils.py       # Funções utilitárias (HTTP, paginação)
├── 📁 tests
│   ├── 🐍 __init__.py
│   └── 🐍 test_router.py # Testes automatizados da API
├── ⚙️ .gitignore
├── 📝 README.md
├── 🐍 main.py            # Inicialização da aplicação FastAPI
└── 📄 requirements.txt   # Dependências do projeto
```

---

## 🐍 Requisitos

* **Python 3.12 ou superior**
* `pip`

---

## Executando a Aplicação Localmente


### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

---

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Ativação do ambiente virtual (bash):

```bash
source .venv/scripts/Activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar a aplicação

```bash
fastapi dev main.py
```

A API estará disponível, por padrão, em:

```
http://127.0.0.1:8000
```

A documentação interativa (SwaggerUI) pode ser acessada em:

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Exemplos de Uso

### Listar recursos com paginação e busca

```http
GET /people?page=1
GET /people?search=vader
```

### Buscar recurso individual

```http
GET /person/1
GET /film/2
```

### Consultar dados relacionais

```http
GET /person/1/films
GET /film/2/characters
GET /planet/2/residents
```

---

## 🧪 Testes Automatizados

Para executar os testes unitários (do script "router.py"):

```bash
pytest
```

Os testes validam:

* Status HTTP
* Estrutura das respostas
* Paginação e busca
* Relacionamentos entre recursos

---

## 📌 Observações

* A API não persiste dados localmente.
* Todas as informações são obtidas dinamicamente da **SWAPI**.
* O projeto foi estruturado com foco em clareza, extensibilidade e boas práticas de backend.
* Em caso de adição de novos recursos na SWAPI, basta adicioná-los no enum de "resources.py" e definir as novas rotas individuais!

---
