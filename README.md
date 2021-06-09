# Тестовое задание Bookstore

## Перед запуском

1. Сконфигурировать docker и docker-compose
2. Создать Postgres базу данных
3. Настроить Redis базу данных
4. В корневой директории проекта создать `.env` файл, содержащий настройки для запуска:
    ```
    DEBUG=TRUE
    DB_NAME=bookstore
    DB_USER=postgres
    DB_PASSWORD=test12345
    DB_HOST=localhost
    DB_PORT=5432
    REDIS_URL=redis://127.0.0.1:6379/0
    SECRET_KEY=django-insecure-3!4qm!9=)wofuei4$-6jdz&naexab3@!i%kt)gre%bm)5)8i&u
    EMAIL_HOST_USER=qlgf3onpum@gmail.com
    EMAIL_HOST_PASSWORD=xQ(6F1aXYi'h8'@}(tWD
    ```

## Запуск
```
sudo docker-compose up --build
```

## Использование API

С документацией к API можно ознакомиться по адресу:

http://127.0.0.1:8000/swagger/

Войти в панель администрирования можно по адресу:

http://127.0.0.1:8000/admin/

используя

```
username: admin
password: test12345
```
