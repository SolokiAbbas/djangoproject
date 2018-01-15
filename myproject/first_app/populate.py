import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firt_app.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage,AccessRecord
from faker import Faker
