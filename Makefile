
APP_NAME := app
APP_TAG := test

build:
	docker build -t $(APP_NAME):$(APP_TAG) .

run:
	( \
		docker network create test && \
		docker run --network test --name test_app -d -p 5000:5000 $(APP_NAME):$(APP_TAG) && \
		docker run --network test --name test_db -d -p 27017:27017 mongo:4 \
	)

clean:
	( \
		docker rm -f test_app test_db && \
		docker network rm test \
	)
