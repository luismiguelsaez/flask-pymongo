
APP_NAME := app
APP_TAG := test

build:
	docker build -t $(APP_NAME):$(APP_TAG) app

run:
	( \
		export APP_NAME=$(APP_NAME) APP_TAG=$(APP_TAG) && \
		docker-compose up -d --build \
	)

testing: run
	docker-compose exec test pytest /test/main.py

clean:
	docker-compose down --rmi local -v
