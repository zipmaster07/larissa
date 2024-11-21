"""Populates the database with `FirearmDetails` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.11'
__creation_date__ = '2024-11-20'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import FirearmDetails

count = 0
added = 0
print('ADDING FIREARM DETAILS TO DATABASE...')
firearm_details = [
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 7,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 10,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 12,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 13,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 15,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 17,
    },
{
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 19,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 20,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 21,
    },
    {
        'sight_type': 0,
        'suppressed': False,
        'magazine_capacity': 30,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 7,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 10,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 12,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 13,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 15,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 17,
    },
{
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 19,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 20,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 21,
    },
    {
        'sight_type': 1,
        'suppressed': False,
        'magazine_capacity': 30,
    },
    {
        'sight_type': 1,
        'suppressed': True,
        'magazine_capacity': 20,
    },
    {
        'sight_type': 1,
        'suppressed': True,
        'magazine_capacity': 30,
    },
]

for firearm_detail in firearm_details:
    count += 1
    fd = FirearmDetails(**firearm_detail)
    try:
        print(f"{count}: Adding '{fd}' to database.")
        fd.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{fd}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{fd}' to the database.\n{e}\n")

print(f"ADDED {added} FIREARM DETAIL(S) TO DATABASE.")