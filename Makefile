
APP_NAME := app
APP_TAG := test

build:
	docker build -t $(APP_NAME):$(APP_TAG) app

run:
	docker-compose up -d --build

test:
	docker-compose exec test pytest /test/main.py

clean:
	docker-compose down --rmi local -v
