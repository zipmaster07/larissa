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
from scoring.models import Caliber, Firearm, FirearmDetails, FirearmType

count = 0
added = 0
print('ADDING FIREARMS TO DATABASE...')
_9mm = Caliber.objects.get(short_name='9mm')
_40 = Caliber.objects.get(short_name='.40')
_556 = Caliber.objects.get(short_name='5.56')
pistol = FirearmType.objects.get(type='Pistol')
rifle = FirearmType.objects.get(type='Rifle')
irons_unsup_mag_10 = FirearmDetails.objects.get(sight_type=0,suppressed=False,magazine_capacity=10)
irons_unsup_mag_13 = FirearmDetails.objects.get(sight_type=0,suppressed=False,magazine_capacity=13)
irons_unsup_mag_15 = FirearmDetails.objects.get(sight_type=0,suppressed=False,magazine_capacity=15)
irons_unsup_mag_17 = FirearmDetails.objects.get(sight_type=0,suppressed=False,magazine_capacity=17)
irons_unsup_mag_30 = FirearmDetails.objects.get(sight_type=0,suppressed=False,magazine_capacity=30)
red_unsup_mag_30 = FirearmDetails.objects.get(sight_type=1,suppressed=False,magazine_capacity=30)
red_sup_mag_30 = FirearmDetails.objects.get(sight_type=1,suppressed=True,magazine_capacity=30)


firearms = [
    {
        'type': pistol,
        'caliber': _9mm,
        'firearm_details': irons_unsup_mag_15,
        'manufacturer': 'Glock',
        'model': '19',
        'barrel_length': 4.02,
        'trigger_action': 0,
    },
    {
        'type': pistol,
        'caliber': _40,
        'firearm_details': irons_unsup_mag_13,
        'manufacturer': 'Glock',
        'model': '23',
        'barrel_length': 4.02,
        'trigger_action': 0
    },
    {
        'type': pistol,
        'caliber': _9mm,
        'firearm_details': irons_unsup_mag_17,
        'manufacturer': 'FN',
        'model': '509 Tactical',
        'barrel_length': 4.5,
        'trigger_action': 0,
    },
    {
        'type': pistol,
        'caliber': _9mm,
        'firearm_details': irons_unsup_mag_10,
        'manufacturer': 'Sig Sauer',
        'model': 'P365',
        'barrel_length': 3.1,
        'trigger_action': 0,
    },
    {
        'type': pistol,
        'caliber': _9mm,
        'firearm_details': irons_unsup_mag_10,
        'manufacturer': 'Sig Sauer',
        'model': 'P365XL',
        'barrel_length': 3.7,
        'trigger_action': 0,
    },
    {
        'type': pistol,
        'caliber': _9mm,
        'firearm_details': irons_unsup_mag_10,
        'manufacturer': 'Smith & Wesson',
        'model': 'Shield Plus',
        'barrel_length': 3.1,
        'trigger_action': 0,
    },
    {
        'type': pistol,
        'caliber': _9mm,
        'firearm_details': irons_unsup_mag_10,
        'manufacturer': 'Smith & Wesson',
        'model': 'Shield Plus',
        'barrel_length': 4,
        'trigger_action': 0,
    },
    {
        'type': rifle,
        'caliber': _556,
        'firearm_details': irons_unsup_mag_30,
        'manufacturer': 'Custom',
        'model': 'AR-15',
        'barrel_length': 16,
        'trigger_action': 1,
    },
    {
        'type': rifle,
        'caliber': _556,
        'firearm_details': red_unsup_mag_30,
        'manufacturer': 'Custom',
        'model': 'AR-15',
        'barrel_length': 16,
        'trigger_action': 1,
    },
    {
        'type': rifle,
        'caliber': _556,
        'firearm_details': red_sup_mag_30,
        'manufacturer': 'Custom',
        'model': 'AR-15',
        'barrel_length': 16,
        'trigger_action': 1,
    },
    {
        'type': rifle,
        'caliber': _556,
        'firearm_details': red_unsup_mag_30,
        'manufacturer': 'Custom',
        'model': 'Mk 18',
        'barrel_length': 10.3,
        'trigger_action': 1,
    },
    {
        'type': rifle,
        'caliber': _556,
        'firearm_details': red_sup_mag_30,
        'manufacturer': 'Custom',
        'model': 'Mk 18',
        'barrel_length': 10.3,
        'trigger_action': 1,
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