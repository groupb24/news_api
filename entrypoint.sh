set -o errexit
set -o pipefail
set -o nounset

export DJANGO_SETTINGS_MODULE=config.settings.custom

python manage.py collectstatic --noinput

python manage.py makemigrations
python manage.py migrate

gunicorn config.wsgi:application --bind 0.0.0.0:8080