# Blink

Blink tools for citizen participation.

* bettertext - text improvement

## Using docker-compose in production

    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

    docker-compose -f docker-compose.prod.yml logs -f

## Develop environment

    docker-compose down -v
    docker-compose up -d --build
    docker-compose exec web python manage.py migrate --noinput

    # Usefull commands
    docker-compose exec web python manage.py shell -c "from accounts.models import MyUser; MyUser.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
    docker-compose exec web python manage.py startapp some_new_app
    docker-compose exec db psql --username=blink --dbname=blink_dev
