"""Populates the database with the `Firearm` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Firearm, FirearmType

count = 0
added = 0
print('ADDING FIREARMS TO DATABASE...')
sidearm = FirearmType.objects.get(type='Sidearm')
long_gun = FirearmType.objects.get(type='Long gun')

firearms = [
    {
        'model': '19',
        'manufacturer': 'Glock',
        'type': sidearm,
    },
    {
        'model': '23',
        'manufacturer': 'Glock',
        'type': sidearm,
    },
    {
        'model': '509 Tactical',
        'manufacturer': 'FN',
        'type': sidearm,
    },
    {
        'model': 'P365',
        'manufacturer': 'Sig Sauer',
        'type': sidearm,
    },
    {
        'model': 'P365XL',
        'manufacturer': 'Sig Sauer',
        'type': sidearm,
    },
    {
        'model': 'AR-15',
        'manufacturer': 'Custom',
        'type': long_gun,
    },
]

for firearm in firearms:
    count += 1
    f = Firearm(**firearm)
    try:
        print(f"{count}: Adding '{f}' to database.")
        f.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{f}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{f}' to the database.\n{e}\n")

print(f"ADDED {added} FIREARM(S) TO DATABASE.")