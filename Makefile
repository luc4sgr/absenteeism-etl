.PHONY: run test coverage clean

# Executa o pipeline
run:
	poetry run python scripts/run_pipeline.py

# Roda os testes unitários
test:
	poetry run pytest

# Gera relatório de cobertura
coverage:
	poetry run pytest --cov=app --cov-report=term-missing

# Remove arquivos de cache e outputs temporários
clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -name '*.pyc' -delete
