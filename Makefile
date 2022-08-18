IMAGE=ektowett/djcart:latest

build:
	docker build -t $(IMAGE) .

up:
	docker-compose up -d

ps:
	docker-compose ps

migrate:
	docker-compose exec app python manage.py migrate

makemigrations:
	docker-compose exec app python manage.py makemigrations

collectstatic:
	docker-compose exec app python manage.py collectstatic --noinput

createsuperuser:
	docker-compose exec app python manage.py createsuperuser

logs:
	docker-compose logs -f

rm: stop
	docker-compose rm -f

stop:
	docker-compose stop
