echo "Waiting for postgres..."

sleep 30


python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
exec "$@"