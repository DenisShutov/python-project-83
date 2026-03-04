#установка заисимостей
install:
	uv sync

#Используйте эту команду, 
#чтобы запускать приложение в режиме отладки в процессе разработки
dev:
	uv run flask --debug --app page_analyzer:app run

lint:
	uv run ruff check page_analyzer

lint-fix:
	uv run ruff check --fix page_analyzer

#Эта команда запускает приложение уже в режиме продакшена. 
#Приложение будет доступно по адресу http://localhost:8000, 
#если в переменных окружения не указан порт, необходимый для деплоя.
PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

# скачиваем uv и запускаем команду установки зависимостей
build:
	./build.sh

#Прямой вызов gunicorn (без uv)
render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app