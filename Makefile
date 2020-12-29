#!make

include ENVIRONMENT  
export $(shell sed 's/=.*//' envfile)

build:
	docker build -t ${APP_NAME}:${APP_TAG} app

run:
	( \
		export APP_NAME=${APP_NAME} APP_TAG=${APP_TAG} && \
		docker-compose up -d \
	)

testing: run
	docker-compose exec test pytest /test/main.py

clean:
	docker-compose down --rmi local -v

deploy:
	kubectl apply -f k8s
