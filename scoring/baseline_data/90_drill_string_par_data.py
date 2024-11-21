"""Populates the database with the `StringParTime` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Drill, DrillString, DrillStringPar, FirearmType

count = 0
added = 0
print('ADDING STRING PAR TIMES TO DATABASE...')

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
check_down = Drill.objects.get(name='Check Down')
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

pistol = FirearmType.objects.get(type='Pistol')
rifle = FirearmType.objects.get(type='Rifle')

string_par_times = [
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'par': 3.5,
        'firearm_type': rifle,
        'note': 'Beginner'

    },
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'par': 2.5,
        'firearm_type': rifle,
        'note': 'Intermediate'
    },
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'par': 1.5,
        'firearm_type': rifle,
        'note': 'Advanced'
    },
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'par': 5,
        'firearm_type': pistol,
        'note': 'Beginner'
    },
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'par': 4,
        'firearm_type': pistol,
        'note': 'Intermediate'
    },
    {
        'string': DrillString.objects.get(drill=_2x2x2, seqno=1),
        'par': 3.5,
        'firearm_type': pistol,
        'note': 'Advanced'
    },
    {
        'string': DrillString.objects.get(drill=_3M, seqno=1),
        'par': 18,
        'firearm_type': None,
        'note': 'Beginner'
    },
    {
        'string': DrillString.objects.get(drill=_3M, seqno=1),
        'par': 15,
        'firearm_type': None,
        'note': 'Experienced'
    },
    {
        'string': DrillString.objects.get(drill=_3M, seqno=1),
        'par': 12,
        'firearm_type': None,
        'note': 'Instructor'
    },
    {
        'string': DrillString.objects.get(drill=_5x5, seqno=1),
        'par': 5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=_9hole, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=active_shooter, seqno=1),
        'par': 13,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=bill_drill, seqno=1),
        'par': 3.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=bright_light, seqno=1),
        'par': 4,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cadence_drill, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=casino, seqno=1),
        'par': 21,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cold_start, seqno=1),
        'par': 15,
        'firearm_type': None,
        'note': 'Beginner'
    },
    {
        'string': DrillString.objects.get(drill=cold_start, seqno=1),
        'par': 12,
        'firearm_type': None,
        'note': 'Intermediate'
    },
    {
        'string': DrillString.objects.get(drill=cold_start, seqno=1),
        'par': 10,
        'firearm_type': None,
        'note': 'Expert'
    },
    {
        'string': DrillString.objects.get(drill=check_down, seqno=1),
        'par': 12,
        'firearm_type': None,
        'note': 'Standard'
    },
    {
        'string': DrillString.objects.get(drill=check_down, seqno=1),
        'par': 10,
        'firearm_type': None,
        'note': 'Advanced'
    },
    {
        'string': DrillString.objects.get(drill=check_down, seqno=1),
        'par': 8,
        'firearm_type': None,
        'note': 'Elite'
    },
    {
        'string': DrillString.objects.get(drill=collateral, seqno=1),
        'par': 2.5,
        'firearm_type': None,
        'note': 'Expert'
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=2),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=3),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=4),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=5),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=6),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=7),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=cornucopia, seqno=8),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=2),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=3),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=4),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=5),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=6),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=dot_torture, seqno=7),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=el_presidente, seqno=1),
        'par': 10,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=1),
        'par': 3,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=2),
        'par': 8,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=3),
        'par': 3,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=4),
        'par': 4,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=5),
        'par': 8,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=6),
        'par': 6,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=7),
        'par': 8,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=fbi_qual, seqno=8),
        'par': 15,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=first_shot, seqno=1),
        'par': 2,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=five_yard_roundup, seqno=1),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=five_yard_roundup, seqno=2),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=five_yard_roundup, seqno=3),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=five_yard_roundup, seqno=4),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=mozambique, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=runenation, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=super_test, seqno=1),
        'par': 15,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=super_test, seqno=2),
        'par': 10,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=super_test, seqno=3),
        'par': 5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=the_burger_drill, seqno=1),
        'par': 16,
        'firearm_type': rifle,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=throttle_control, seqno=1),
        'par': None,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=1),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=2),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=3),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
    {
        'string': DrillString.objects.get(drill=wizard, seqno=4),
        'par': 2.5,
        'firearm_type': None,
        'note': ''
    },
]

for string_par_time in string_par_times:
    count += 1
    spt = DrillStringPar(**string_par_time)
    try:
        print(f"{count}: Adding '{spt}' to database.")
        spt.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{spt}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{spt}' to the database.\n{e}\n")

print(f"ADDED {added} STRING PAR TIME(S) TO DATABASE.")