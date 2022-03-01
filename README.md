
## Локальный запуск

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt  
    $ python manage.py migrate
    $ python manage.py runserver

## Добавить администратора

    $ python manage.py createsuperuser
Дальше по описанию

## Зайти в админку и накидать вручную работы, группы и результаты

Перейти на /admin, зайти под учеткой которую создали в предыдущем шаге.
Дальше слева потыкать на StudentGroup, Lab, LabResult вкладки и дальше все интуитивно

