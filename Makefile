
APP_NAME := app
APP_TAG := test

build:
	docker build -t $(APP_NAME):$(APP_TAG) .

run-docker:
	( \
		docker network create test && \
		docker run --network test --name test_app -e MONGO_HOST=test_db -e MONGO_DB=invest -d -p 5000:5000 $(APP_NAME):$(APP_TAG) && \
		docker run --network test --name test_db -d -p 27017:27017 mongo:4 \
	)

run:
	docker-compose up -d --build

test:
	pytest code/test.py

clean-docker:
	( \
		docker rm -f test_app test_db && \
		docker network rm test \
	)

clean:
	docker-compose down
