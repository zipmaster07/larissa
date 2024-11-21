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
from scoring.models import Drill, DrillString, DrillStringDistance

count = 0
added = 0
print('ADDING STRING DISTANCES TO DATABASE...')

_2x2x2 = Drill.objects.get(name='2x2x2')
_3M = Drill.objects.get(name='3M')
_5x5 = Drill.objects.get(name='5x5')
_9hole = Drill.objects.get(name='9-Hole')
active_shooter = Drill.objects.get(name='Active Shooter')
bill_drill = Drill.objects.get(name='Bill Drill')
bright_light = Drill.objects.get(name='Bright Light')
cadence_drill = Drill.objects.get(name='Cadence Drill')
casino = Drill.objects.get(name='Casino')
check_down = Drill.objects.get(name='Check Down')
cold_start = Drill.objects.get(name='Cold Start')
collateral = Drill.objects.get(name='Collateral')
cornucopia = Drill.objects.get(name='Cornucopia')
dot_torture = Drill.objects.get(name='Dot Torture')
el_presidente = Drill.objects.get(name='El Presidente')
fbi_qual = Drill.objects.get(name='FBI Qualification')
first_shot = Drill.objects.get(name='First Shot')
five_yard_roundup = Drill.objects.get(name='Five-yard Roundup')
mozambique = Drill.objects.get(name='Mozambique')
runenation = Drill.objects.get(name='Runenation')
super_test = Drill.objects.get(name='Super Test')
the_burger_drill = Drill.objects.get(name='The Burger Drill')
throttle_control = Drill.objects.get(name='Throttle Control')
wizard = Drill.objects.get(name='Wizard')

string_distances = [
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=_3M, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=_5x5, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=_9hole, seqno=1),
        'start_distance': 50,
        'end_distance': 50,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=active_shooter, seqno=1),
        'start_distance': 40,
        'end_distance': 10,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=bill_drill, seqno=1),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=bright_light, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cadence_drill, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=casino, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=check_down, seqno=1),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cold_start, seqno=1),
        'start_distance': 10,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=collateral, seqno=1),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=2),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=3),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=4),
        'start_distance': 10,
        'end_distance': 10,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=5),
        'start_distance': 10,
        'end_distance': 10,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=6),
        'start_distance': 10,
        'end_distance': 20,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=7),
        'start_distance': 20,
        'end_distance': 20,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=8),
        'start_distance': 20,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=1),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=2),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=3),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=4),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=5),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=6),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=7),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=el_presidente, seqno=1),
        'start_distance': 10,
        'end_distance': 10,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=1),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=2),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=3),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=4),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=5),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=6),
        'start_distance': 15,
        'end_distance': 15,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=7),
        'start_distance': 15,
        'end_distance': 15,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=8),
        'start_distance': 26,
        'end_distance': 25,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=first_shot, seqno=1),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=five_yard_roundup, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=mozambique, seqno=1),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=runenation, seqno=1),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=super_test, seqno=1),
        'start_distance': 15,
        'end_distance': 15,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=super_test, seqno=2),
        'start_distance': 10,
        'end_distance': 10,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=super_test, seqno=3),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=the_burger_drill, seqno=1),
        'start_distance': 25,
        'end_distance': 10,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=throttle_control, seqno=1),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=1),
        'start_distance': 3,
        'end_distance': 3,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=2),
        'start_distance': 5,
        'end_distance': 5,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=3),
        'start_distance': 7,
        'end_distance': 7,
        'distance_type': 0
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=4),
        'start_distance': 10,
        'end_distance': 10,
        'distance_type': 0
    },
]

for string_distance in string_distances:
    count += 1
    sd = DrillStringDistance(**string_distance)
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