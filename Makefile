.PHONY: install test lint format api frontend ingest docker-build docker-up docker-down

install:
	pip install -r requirements.txt

test:
	pytest -v --cov=src/multimodal_assistant --cov-report=term-missing

lint:
	ruff check src tests
	mypy src

format:
	ruff format src tests

api:
	uvicorn multimodal_assistant.api.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src

frontend:
	streamlit run src/multimodal_assistant/frontend/app.py

ingest:
	python scripts/run_ingestion.py

docker-build:
	docker compose build

docker-up:
	docker compose up --build

docker-down:
	docker compose down
