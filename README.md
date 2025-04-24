# 🧩 Absenteeism ETL

Pipeline ETL modular e testável para consolidação de dados tabulares (Excel), com arquitetura orientada a interfaces e CLI amigável. Ideal para processar dados como ausências, despesas e outras categorias.

---

## 🚀 Funcionalidades

- Processa múltiplos arquivos `.xlsx` em subpastas organizadas por tipo
- Consolida em um único arquivo final (por tipo)
- Gera dados sintéticos para testes
- CLI poderosa com `typer`
- Logging estruturado
- Testes com `pytest` e `coverage`
- Estrutura modular com interfaces e boas práticas

---

## 🔧 Tecnologias

- Python 3.12
- [Poetry](https://python-poetry.org/)
- pandas, openpyxl
- faker
- typer (CLI)
- pytest, pytest-cov

---

## 🗂️ Estrutura

```plaintext
app/
├── cli.py                      # Interface de linha de comando
├── core/                       # Interfaces base e logger
├── extractors/                 # Extractors por formato (Excel, etc)
├── loaders/                    # Loaders (salvamento em .xlsx)
├── pipeline/                   # Orquestração do processo ETL
├── transformers/               # Transformadores (concatenação, etc)
├── utils/                      # Geradores de dados sintéticos
data/
├── input/<tipo>/              # Arquivos de entrada (por tipo)
└── output/<tipo>/             # Arquivo consolidado de saída (por tipo)
```

---

## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/absenteeism-etl.git
cd absenteeism-etl

# Instale o Poetry se ainda não tiver
pip install poetry

# Instale as dependências
poetry install

# Ative o ambiente virtual
poetry shell
```

---

## 🖥️ Comandos úteis (via CLI)

### ✅ Gerar dados sintéticos
```bash
poetry run etl generate-data --tipo ausencias --count 20
```

### ✅ Rodar o ETL completo
```bash
poetry run etl run --tipo ausencias --file ausencias_maio.xlsx
```

### ✅ Ver ajuda da CLI
```bash
poetry run etl --help
```

---

## 🧪 Testes e qualidade

```bash
# Rodar os testes
poetry run pytest

# Verificar cobertura de código
poetry run pytest --cov=app --cov-report=term-missing
```

---

## 🔄 Atalhos com Makefile

```bash
make run        # Executa o pipeline
make test       # Roda os testes
make coverage   # Mostra cobertura
make clean      # Remove arquivos temporários
```

---

## 📄 Licença

MIT © Lucas Granjense

---

