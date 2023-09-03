"""Populates the database with the `StringDistance` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Drill, String, StringDistance

count = 0
added = 0
print('ADDING STRING DISTANCES TO DATABASE...')

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

string_distances = [
    {
        'string': String.objects.get(drill=_2x2x2, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=_2x2x2, seqno=1),
        'starting_distance': 7,
        'ending_distance': 7,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=_3M, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=_5x5, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=bill_drill, seqno=1),
        'starting_distance': 7,
        'ending_distance': 7,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=cadence_drill, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=casino, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=cold_start, seqno=1),
        'starting_distance': 10,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=1),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=2),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=3),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=4),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=5),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=6),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=dot_torture, seqno=7),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=el_presidente, seqno=1),
        'starting_distance': 10,
        'ending_distance': 10,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=1),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=2),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=3),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=4),
        'starting_distance': 7,
        'ending_distance': 7,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=5),
        'starting_distance': 7,
        'ending_distance': 7,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=6),
        'starting_distance': 15,
        'ending_distance': 15,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=7),
        'starting_distance': 15,
        'ending_distance': 15,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=fbi_qual, seqno=8),
        'starting_distance': 26,
        'ending_distance': 25,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=first_shot, seqno=1),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=five_yard_roundup, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=2),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=3),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=4),
        'starting_distance': 10,
        'ending_distance': 10,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=5),
        'starting_distance': 10,
        'ending_distance': 10,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=6),
        'starting_distance': 10,
        'ending_distance': 20,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=7),
        'starting_distance': 20,
        'ending_distance': 20,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=mr_toads_drill, seqno=8),
        'starting_distance': 20,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=super_test, seqno=1),
        'starting_distance': 15,
        'ending_distance': 15,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=super_test, seqno=2),
        'starting_distance': 10,
        'ending_distance': 10,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=super_test, seqno=3),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=the_burger_drill, seqno=1),
        'starting_distance': 25,
        'ending_distance': 10,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=throttle_control, seqno=1),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=wizard, seqno=1),
        'starting_distance': 3,
        'ending_distance': 3,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=wizard, seqno=2),
        'starting_distance': 5,
        'ending_distance': 5,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=wizard, seqno=3),
        'starting_distance': 7,
        'ending_distance': 7,
        'distance_type': 0
    },
    {
        'string': String.objects.get(drill=wizard, seqno=4),
        'starting_distance': 10,
        'ending_distance': 10,
        'distance_type': 0
    },
]

for string_distance in string_distances:
    count += 1
    sd = StringDistance(**string_distance)
    try:
        print(f"{count}: Adding '{sd}' to database.")
        sd.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{sd}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{sd}' to the database.\n{e}\n")

print(f"ADDED {added} STRING DISTANCE(S) TO DATABASE.")