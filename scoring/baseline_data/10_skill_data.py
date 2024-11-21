"""Populates the database with the `Skill` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-07-30'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Skill

count = 0
added = 0
print('ADDING SKILLS TO DATABASE...')
skills = [
    ('sight alignment', 'Sight alignment occurs when the shooter assumes a proper grip on the pistol and aims downrange. As the shooter’s eye lines up with the rear sight aperture, the front sight post will become visible in the notch. Proper sight alignment is achieved when the shooter aligns the front sight post within the rear sight aperture, having equal space (or light) on either side of the post, and the top of the front sight post even with the ‘shoulders’ of the rear aperture. Right before the shooter fires, the shooter will focus exclusively on the front sight post.'),
    ('sight picture', 'Sight picture, as a concept, is when the sights are properly aligned and aimed at an intended spot on an intended target. The “picture” of pistol sight picture refers to what the shooter’s eye will see: fuzzy rear sight, focused front sight, and fuzzy target.'),
    ('trigger control', 'Trigger control refers to the act of moving the trigger and firing a gun without disturbing the sights.'),
    ('target acquisition', 'Target acquisition is the detection and identification of the location of a target in sufficient detail to permit the effective employment of lethal and non-lethal means. The term is used for a broad area of applications.'),
    ('target transition', ''),
    ('marksmanship', 'The ability to shoot accurately at a target.'),
    ('movement', 'Movement teaches the shooter to move as to avoid being an easy target and during key opportunities such when reloading and during a malfunction.'),
    ('manipulation', 'Manipulation is the level of proficency to operate the firearm.'),
    ('draw stroke', 'Draw stroke is how a sidearm is drawn from a holster (concealed or duty). Proper draw stroke can be broken down into 4 or 5 distinct steps depending on style and instructor.'),
    ('recoil management', 'Recoil management aims to increase the precision of your shooting by limiting muzzle rise when you fire the gun.'),
    ('reloading', 'Reloading involves training to increase the speed of the reload, whether it is a tactical or emergency reload.'),
    ('emergency reloads', 'The act of reloading a firearm because the current magazine no longer has ammunition and the firearm has run dry. An emergency reload means the bolt or slide has been locked.'),
    ('accuracy', 'The ability to put shots on the intended target as quickly as possible.'),
    ('mental discipline', 'Mental discipline is the skill used to keep focus on the immediate task at hand even when unforeseen events or malfunctions are taking place.'),
    ('muzzle discipline', 'Muzzle discipline is the skill used to ensure that the muzzle of the firearm is always pointed in a safe and proper direction, even when rapid movement is required during a situation'),
    ('stance', ''),
    ('grip', ''),
    ('cadence', ''),
    ('fitness', 'The level of physical fitness an individual has and how well a shooter can perform while physically fatigued.'),
    ('weapons manipulation', ''),
    ('kit shakeout', ''),
]

for skill in skills:
    count += 1
    s = Skill(name = skill[0], description=skill[1])
    try:
        print(f"{count}: Adding '{s}' to database.")
        s.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{s}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{s}' to the database.\n{e}\n")

print(f"ADDED {added} SKILL(S) TO DATABASE.")