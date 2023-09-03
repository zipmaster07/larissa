"""Populates the database with the `History` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from datetime import date
from django.db.utils import IntegrityError
from scoring.models import Drill, History

count = 0
added = 0
print('ADDING HISTORY TO DATABASE...')

_2x2x2 = Drill.objects.get(name='2x2x2')
_3M = Drill.objects.get(name='3M')
_5x5 = Drill.objects.get(name='5x5')
bill_drill = Drill.objects.get(name='Bill Drill')
cadence_drill = Drill.objects.get(name='Cadence Drill')
casino = Drill.objects.get(name='Casino')
cold_start = Drill.objects.get(name='Cold Start')
dot_torture = Drill.objects.get(name='Dot Torture')
el_presidente = Drill.objects.get(name='El Presidente')
fbi_qual = Drill.objects.get(name='FBI Qualification')
first_shot = Drill.objects.get(name='First Shot')
five_yard_roundup = Drill.objects.get(name='Five-yard Roundup')
mr_toads_drill = Drill.objects.get(name="Mr. Toad's Drill")
super_test = Drill.objects.get(name='Super Test')
the_burger_drill = Drill.objects.get(name='The Burger Drill')
throttle_control = Drill.objects.get(name='Throttle Control')
wizard = Drill.objects.get(name='Wizard')

history = [
    {
        'event_date': date(2022,2,19),
        'drill': dot_torture,
        'count': 1,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,2,19),
        'drill': casino,
        'count': 3,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,2,19),
        'drill': five_yard_roundup,
        'count': 4,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,3,19),
        'drill': dot_torture,
        'count': 1,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,3,19),
        'drill': wizard,
        'count': 4,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,4,16),
        'drill': dot_torture,
        'count': 1,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,4,16),
        'drill': wizard,
        'count': 4,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,4,16),
        'drill': _3M,
        'count': 3,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,5,26),
        'drill': dot_torture,
        'count': 1,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,5,26),
        'drill': throttle_control,
        'count': 2,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,5,26),
        'drill': _3M,
        'count': 2,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,5,26),
        'drill': cadence_drill,
        'count': 2,
        'location': 'Unknown'
    },
    {
        'event_date': date(2022,6,11),
        'drill': mr_toads_drill,
        'count': 1,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,6,11),
        'drill': _3M,
        'count': 2,
        'location': 'Saratoga Springs',
    },
    {
        'event_date': date(2022,6,11),
        'drill': casino,
        'count': 2,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,6,25),
        'drill': mr_toads_drill,
        'count': 1,
        'location': 'Spanish Fork'
    },
    {
        'event_date': date(2022,6,25),
        'drill': five_yard_roundup,
        'count': 4,
        'location': 'Spanish Fork'
    },
    {
        'event_date': date(2022,6,25),
        'drill': wizard,
        'count': 4,
        'location': 'Spanish Fork'
    },
    {
        'event_date': date(2022,6,25),
        'drill': throttle_control,
        'count': 1,
        'location': 'Spanish Fork'
    },
    {
        'event_date': date(2022,7,23),
        'drill': bill_drill,
        'count': 4,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,7,23),
        'drill': _3M,
        'count': 3,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,7,23),
        'drill': five_yard_roundup,
        'count': 5,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,7,23),
        'drill': wizard,
        'count': 3,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,11,11),
        'drill': mr_toads_drill,
        'count': 1,
        'location': 'Spanish Fork'
    },
    {
        'event_date': date(2022,11,11),
        'drill': wizard,
        'count': 4,
        'location': 'Spanish Fork'
    },
    {
        'event_date': date(2022,12,10),
        'drill': mr_toads_drill,
        'count': 1,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,12,10),
        'drill': casino,
        'count': 2,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2022,12,10),
        'drill': _3M,
        'count': 3,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,4,22),
        'drill': dot_torture,
        'count': 1,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,4,22),
        'drill': first_shot,
        'count': 20,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,4,22),
        'drill': wizard,
        'count': 3,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,4,22),
        'drill': _3M,
        'count': 3,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,6,4),
        'drill': the_burger_drill,
        'count': 5,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,6,4),
        'drill': _3M,
        'count': 6,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,6,4),
        'drill': wizard,
        'count': 5,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,7,21),
        'drill': fbi_qual,
        'count': 1,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,7,21),
        'drill': casino,
        'count': 2,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,7,21),
        'drill': wizard,
        'count': 2,
        'location': 'Saratoga Springs'
    },
    {
        'event_date': date(2023,7,21),
        'drill': throttle_control,
        'count': 1,
        'location': 'Saratoga Springs'
    },
]

for event in history:
    count += 1
    h = History(**event)
    try:
        print(f"{count}: Adding '{h}' to database.")
        h.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{h}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{h}' to the database.\n{e}\n")

print(f"ADDED {added} EVENT(S) TO DATABASE.")