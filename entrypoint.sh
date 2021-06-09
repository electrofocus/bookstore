python manage.py migrate
python manage.py collectstatic --noinput

while :;
  do exec gunicorn bookstore.wsgi --bind=0.0.0.0:8000
done;
