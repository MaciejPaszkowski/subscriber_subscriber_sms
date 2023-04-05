# subscriber_subscriber_sms

#konfiguracja projektu
python3 -m venv venc
source venv/bin/activate

pip -r requirements.txt

cd subscriber_core
python manage.py migrate

# uruchomienie api
python manage.py runserver

# opis API:
- /subscribers            [GET, POST]
- /subscribers/{id}       [GET, PUT, PATCH, DELETE]
- /subscribers-sms        [GET, POST]
- /subscribers-sms/{id}   [GET, PUT, PATCH, DELETE]
- /clients                [GET, POST]
- /clients/{id}           [GET, PUT, PATCH, DELETE]
- /users                  [GET, POST]
- /users/{id}             [GET, PUT, PATCH, DELETE]


zadanie 1:
python manage.py task1

zadanie 2:
python manage.py task2


testy:
pytest