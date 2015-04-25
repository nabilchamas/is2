#!/bin/bash
python manage.py loaddata pop_db.json
python manage.py test