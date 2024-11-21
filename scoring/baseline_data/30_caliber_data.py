"""Populates the database with the `Caliber` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.11'
__creation_date__ = '2024-11-20'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Caliber

count = 0
added = 0
print('ADDING CALIBERS TO DATABASE...')
calibers = [
    {
        'short_name': '9mm',
        'full_name': '9x19mm Parabellum',
        'description': None,
    },
    {
        'short_name': '.40',
        'full_name': '.40 S&W',
        'description': None,
    },
    {
        'short_name': '5.56',
        'full_name': '5.56x45mm NATO',
        'description': None,
    },
]

for caliber in calibers:
    count += 1
    c = Caliber(**caliber)
    try:
        print(f"{count}: Adding '{c}' to database.")
        c.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{c}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{c}' to the database.\n{e}\n")

print(f"ADDED {added} CALIBER(S) TO DATABASE.")