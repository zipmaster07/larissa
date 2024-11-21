"""Populates the database with the `FirearmType` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import FirearmType

count = 0
added = 0
print('ADDING FIREARM TYPES TO DATABASE...')
firearm_types = ['Pistol', 'Rifle', 'Shotgun', 'Revolver', 'Other']

for firearm_type in firearm_types:
    count += 1
    ft = FirearmType(type=firearm_type)
    try:
        print(f"{count}: Adding '{ft}' to database.")
        ft.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{ft}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{ft}' to the database.\n{e}\n")

print(f"ADDED {added} FIREARM TYPE(S) TO DATABASE.")