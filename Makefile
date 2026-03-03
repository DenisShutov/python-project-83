install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run

lint:
	uv run ruff check page_analyzer

lint-fix:
	uv run ruff check --fix page_analyzer