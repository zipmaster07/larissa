"""Populates the database with the `Shooter` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Shooter

count = 0
added = 0
print('ADDING SHOOTERS TO DATABASE...')

shooters = [
    ('Joshua', 'Schaeffer'),
    ('Daniel', 'Schaeffer'),
    ('Paul', 'Schaeffer'),
    ('Chad', 'Krupa'),
    ('Robert', 'Krupa'),
    ('Jaymes', 'Mosher'),
]

for shooter in shooters:
    count += 1
    s = Shooter(first_name=shooter[0], last_name=shooter[1])
    try:
        print(f"{count}: Adding '{s}' to database.")
        s.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{s}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{s}' to the database.\n{e}\n")

print(f"ADDED {added} SHOOTER(S) TO DATABASE.")