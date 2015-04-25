#!/bin/bash
createdb is2_produccion
python manage.py migrate
