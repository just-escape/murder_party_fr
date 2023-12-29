python manage.py dumpdata --indent 2 murder auth.user > fixtures.json
python manage.py loaddata fixtures.json
