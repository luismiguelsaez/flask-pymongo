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
	( \
		kubectl apply -f k8s/database.yml && \
		envsubst < k8s/application.yml | kubectl apply -f - \
	)

rollback:
	( \
		envsubst < k8s/application.yml | kubectl delete -f - && \
		kubectl delete -f k8s/database.yml \
	)
