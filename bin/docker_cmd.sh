#!/bin/sh

fixtures_dir=${FIXTURES_DIR:-./fixtures}

# Load any JSON fixtures present
if [ -d $fixtures_dir ]; then
    echo "Loading fixtures from $fixtures_dir"

    for fixture in $(ls "$fixtures_dir/"*.json)
    do
        echo "Loading fixture $fixture"
        python src/manage.py loaddata $fixture
    done
fi

# Start server
# >&2 echo "Starting server"
# uwsgi \
#     --http :$uwsgi_port \
#     --http-keepalive \
#     --manage-script-name \
#     --mount $mountpoint=openzaak.wsgi:application \
#     --static-map /static=/app/static \
#     --static-map /media=/app/media  \
#     --chdir src \
#     --enable-threads \
#     --processes $uwsgi_processes \
#     --threads $uwsgi_threads \
#     --buffer-size=65535

exec "$@"