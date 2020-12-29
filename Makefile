
run:
	docker-compose up -d --build

testing: run
	docker-compose exec test pytest /test/main.py

clean: run testing
	docker-compose down --rmi local -v
