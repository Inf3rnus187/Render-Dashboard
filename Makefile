init:
	docker-compose build
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

rebuild:
	docker-compose down
	docker-compose build
	docker-compose up -d
