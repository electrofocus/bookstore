python3 manage.py migrate

while :;
  do exec gunicorn bookstore.wsgi --bind=0.0.0.0:8000
done;
