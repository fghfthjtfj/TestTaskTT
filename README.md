0.Сайт уже доступен с моего тестового сервера по адресу - http://178.255.222.74:80

1.Скачайте проект git clone https://github.com/fghfthjtfj/TestTaskTT.git

2.Убедиться в доступности портов 80 и 8000.


Запуск через докер.

1.Собрать контейнер докера:

docker compose up --build -d


2.Создать суперпользователя django:
   
docker compose exec web bash

python manage.py createsuperuser

Ввести необходимые данные.

3.Выйти из ввода команд:

exit

4.Открыть сайт:
В windows в браузере перейти по *ip-вашего-сервера*.
В linux (на сервере) curl http://localhost/

5.Админка доступна по пути - *ip-вашего-сервера*/admin


Запуск локально.

1.Создать и активировать виртуальное окружение в директории backend:

python -m venv venv

2.Установить зависимости:

pip install -r requirements.txt

3.Создать базу данных и выполнить миграции (sqlite файл создаётся сам).

python manage.py migrate

4.Загрузить фикстуры:

python manage.py loaddata  main/fixtures/main_fixture.yaml

5.Создать суперпользователя django:

python manage.py createsuperuser

Ввести необходимые данные.

6.Открыть сайт:

Открыть ссылку http://127.0.0.1:8000

7.Админка доступна по пути - http://127.0.0.1:8000/admin
