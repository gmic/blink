# Blink

Blink tools for citizen participation.

* bettertext - text improvement

## Using docker-compose in production

"""bash
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

docker-compose -f docker-compose.prod.yml logs -f
"""

## Develop environment

"""bash
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput

docker-compose exec web python manage.py startapp some_new_app
"""
