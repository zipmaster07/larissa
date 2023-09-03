"""Populates the database with the `String` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Drill, String

count = 0
added = 0
print('ADDING DRILL STRINGS TO DATABASE...')

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

drill_strings = [
    {
        'drill': _2x2x2,
        'seqno': 1,
        'live_round_count': 6,
        'instructions': "To set up the drill, place three targets side by side at even intervals 5 or more yards in front of the firing line. For a rifle, the shooter starts with the rifle butt on his shoulder and the muzzle down. For sidearms, the shooter starts from their duty or conceal holster. For those starting out, try starting from low ready.\n\nAt the buzzer, engage each target in order, with two shots each. Right to left or left to right is the shooter's choice. Most people who have some rifle shooting experience will shoot the drill in about 2.0 to 2.5 seconds the first time through. With practice, 1.5 seconds is a viable goal."
    },
    {
        'drill': _3M,
        'seqno': 1,
        'live_round_count': 9,
        'dummy_round_count': 1,
        'instructions': 'Shooter starts with handgun loaded with 6 live rounds (1 in the chamber, 5 in magazine) and one dummy round in the magazine for a total of 7 rounds. The dummy round cannot be the top round nor the bottom round in the magazine. Someone else should load the magazine so the shooter does not know where in the magazine the dummy round lies.\n\nShooter starts holstered, hands in interview stance. On signal, side step, draw, and fire until a malfunction occurs. On the malfunction, side step, fix it, and continue to fire. When the gun runs empty, side step, perform an emergency reload, and fire 3 additional shots to the chest.'
    },
    {
        'drill': _5x5,
        'seqno': 1,
        'live_round_count': 30,
        'instructions': 'Shoot one group with no time limit to confirm zero. Starting from a low ready position, repeat 5 more times with the 5 second time limit in place.\n\nVariations: For an added challenge, draw from the holster instead of low ready. To test consistency, repeat the drill five times.'
    },
    {
        'drill': bill_drill,
        'seqno': 1,
        'live_round_count': 6,
        'instructions': 'Draw from low ready or conceal, fire six rounds.'
    },
    {
        'drill': cadence_drill,
        'seqno': 1,
        'live_round_count': 25,
        'instructions': 'This drill is to work on a balance of speed and accuracy. Rather than counting in your head when shooting the target, shoot as fast as you can keep rounds inside the circles. On the smaller circles, cadence will slow down. Try to maintain consistency. You’ll want your splits to be something like… .30, .31, .30, .32, etc. Not: .32, .37, .34, .43. Use a shot timer to record your splits by hitting the timer and waiting a second or two and begin the string of fire.'
    },
    {
        'drill': casino,
        'seqno': 1,
        'live_round_count': 21,
        'instructions': 'From the holster, start with 7 rounds loaded in the pistol and two 7 round spare magazines. At the starting buzzer, draw and engage each shape in numerical order starting from 1 up to 6. Fire the number of rounds at each shape equal to the number displayed on that shape. Reload as needed.'
    },
    {
        'drill': cold_start,
        'seqno': 1,
        'live_round_count': 10,
        'instructions': 'Start with 2 rounds in the magazine (chamber a round) and 8 rounds in a spare magazine.\n\nStarting at 10 yards, on the buzzer, draw from concealment and place 1 round in each of the top 3” x 3” boxes. Then, on the move, perform a slide lock reload and place 6 rounds in the T1C logo area by the time you reach the 3 yard line. Once at the 3 yard line, place 1 round in each of the small triangles, using only your right hand and left hand, respectively.'
    },
    {
        'drill': dot_torture,
        'seqno': 1,
        'live_round_count': 5,
        'instructions': 'Dot 1: fire five shots slow fire.'
    },
    {
        'drill': dot_torture,
        'seqno': 2,
        'live_round_count': 5,
        'instructions': 'Dot 2: draw, fire once (execute 5 times).'
    },
    {
        'drill': dot_torture,
        'seqno': 3,
        'live_round_count': 8,
        'instructions': 'Dots 3 & 4: draw, fire once on 3, once on 4 (execute 4 times).'
    },
    {
        'drill': dot_torture,
        'seqno': 4,
        'live_round_count': 5,
        'instructions': 'Dot 5: draw, fire five rounds strong hand only.'
    },
    {
        'drill': dot_torture,
        'seqno': 5,
        'live_round_count': 16,
        'instructions': 'Dots 6 & 7: draw, fire twice on 6, twice on 7 (execute 4 times).'
    },
    {
        'drill': dot_torture,
        'seqno': 6,
        'live_round_count': 5,
        'instructions': 'Dot 8: from low ready, fire five rounds weak hand only.'
    },
    {
        'drill': dot_torture,
        'seqno': 7,
        'live_round_count': 6,
        'instructions': 'Dots 9 & 10: draw, fire once on 9, reload, fire once on 10 (execute 3 times).'
    },
    {
        'drill': el_presidente,
        'seqno': 1,
        'live_round_count': 12,
        'instructions': 'Position three silhouette targets ten yards from the firing line. The targets should be in a straight line with three feet between each target. Stand at the firing line with your back to the center target. At the start signal, turn to face the targets, draw your weapon, and fire two rounds into the “A-zone” (or center torso) of each target. Perform a reload, then fire two more rounds into the A zone of each target. When finished, there should be four rounds in each of the targets. This is a timed drill, so speed does count. The goal is to achieve twelve accurate shots in less than 10 seconds.'
    },
    {
        'drill': fbi_qual,
        'seqno': 1,
        'live_round_count': 6,
        'instructions': 'Draw, fire 3 rounds strong hand only (execute 2 times).'
    },
    {
        'drill': fbi_qual,
        'seqno': 2,
        'live_round_count': 6,
        'instructions': 'Draw, fire 3 rounds strong hand only, transition to support hand only and fire 3 more rounds.'
    },
    {
        'drill': fbi_qual,
        'seqno': 3,
        'live_round_count': 12,
        'instructions': 'Draw, fire 3 rounds (execute 4 times).'
    },
    {
        'drill': fbi_qual,
        'seqno': 4,
        'live_round_count': 8,
        'instructions': 'Draw, fire 4 rounds (execute 2 times).'
    },
    {
        'drill': fbi_qual,
        'seqno': 5,
        'live_round_count': 8,
        'instructions': 'Draw, fire 4 rounds, perform an emergency reload and fire 4 more rounds.'
    },
    {
        'drill': fbi_qual,
        'seqno': 6,
        'live_round_count': 6,
        'instructions': 'Draw, fire 3 rounds (execute 2 times).'
    },
    {
        'drill': fbi_qual,
        'seqno': 7,
        'live_round_count': 4,
        'instructions': 'Draw, fire 4 rounds.'
    },
    {
        'drill': fbi_qual,
        'seqno': 8,
        'live_round_count': 10,
        'instructions': 'Start one or two steps behind the 25 yard line. Step forward to the 25 yard line, draw, fire 2 rounds standing, transition to kneeling and fire 3 more rounds (execute 2 times).'
    },
    {
        'drill': first_shot,
        'seqno': 1,
        'live_round_count': 1,
        'instructions': 'Start from concealment with your hands at your sides. On the buzzer, draw and fire one shot. This drill can be used with different types of targets. If using a silhouette type target shoot for either the body or headshot A zone. If using a ring type target shoot for the bullseye/10 zone. A good par time is 2 seconds but the goal is to be able to consistently shoot in the target range without missing over multiple attempts. Improvements can always be made.'
    },
    {
        'drill': five_yard_roundup,
        'seqno': 1,
        'live_round_count': 1,
        'instructions': 'Draw, fire 1 round.'
    },
    {
        'drill': five_yard_roundup,
        'seqno': 2,
        'live_round_count': 4,
        'instructions': 'From low ready, fire 4 rounds.'
    },
    {
        'drill': five_yard_roundup,
        'seqno': 3,
        'live_round_count': 3,
        'instructions': 'From low ready using strong hand only, fire 3 rounds.'
    },
    {
        'drill': five_yard_roundup,
        'seqno': 4,
        'live_round_count': 2,
        'instructions': 'From low ready using support hand only, fire 2 rounds.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 1,
        'live_round_count': 2,
        'instructions': 'From compressed ready, 2 to left target head box.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 2,
        'live_round_count': 2,
        'instructions': '2 to center target head box.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 3,
        'live_round_count': 2,
        'instructions': '2 to right target head box, one handed.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 4,
        'live_round_count': 10,
        'instructions': 'Engage center target 1 round, left target 2 rounds, right target 3 rounds, back to center target 4 rounds.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 5,
        'live_round_count': 6,
        'instructions': '180 degree turn, 3 rounds into left target, slide-lock reload, 3 rounds into right target.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 6,
        'live_round_count': 4,
        'instructions': '2 rounds into left target, move to 20 yard line, 2 rounds into right target (or vice versa).'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 7,
        'live_round_count': 12,
        'instructions': 'From left/right position, engage 2 on each target, move to next position while reloading, 2 on each target again.'
    },
    {
        'drill': mr_toads_drill,
        'seqno': 8,
        'live_round_count': 12,
        'instructions': 'While moving towards 5 yard line, 4 rounds into each target in any order'
    },
    {
        'drill': super_test,
        'seqno': 1,
        'live_round_count': 10,
        'instructions': 'Fire 10 rounds within 15 seconds at 15 yards.'
    },
    {
        'drill': super_test,
        'seqno': 2,
        'live_round_count': 10,
        'instructions': 'Fire 10 rounds within 10 seconds at 10 yards.'
    },
    {
        'drill': super_test,
        'seqno': 3,
        'live_round_count': 10,
        'instructions': 'Fire 10 rounds within 5 seconds at 5 yards.'
    },
    {
        'drill': the_burger_drill,
        'seqno': 1,
        'live_round_count': 8,
        'instructions': 'Setup two targets next to each other at the same distance from the shooting line. Load 6 rounds into a magazine and chamber a round. Have a spare magazine with at least 2 rounds. Starting at 25 yards, the shooter should have their rifle slung in low- or high-ready. At the buzzer shoot two shots per target and then advance to the 10 yard line. Fire two more shots at either target then perform a bolt lock reload and fire the last two shots on the other  target. If possible, put a barrier at the 10 yard line that the shooter must shoot either over or to the side of it. You can also choose to shoot over the barrier before the reload and around the barrier after.'
    },
    {
        'drill': throttle_control,
        'seqno': 1,
        'live_round_count': 10,
        'instructions': 'From concealment. The goal is to put 4 rounds in the center circle, 2 rounds in the medium circles, and a single round in the small ones. In any order you want. Add 1 second for each miss.'
    },
    {
        'drill': wizard,
        'seqno': 1,
        'live_round_count': 1,
        'instructions': 'One head shot, strong hand only.'
    },
    {
        'drill': wizard,
        'seqno': 2,
        'live_round_count': 1,
        'instructions': 'One head shot using both hands on the gun.'
    },
    {
        'drill': wizard,
        'seqno': 3,
        'live_round_count': 1,
        'instructions': 'One head shot using both hands on the gun.'
    },
    {
        'drill': wizard,
        'seqno': 4,
        'live_round_count': 2,
        'instructions': 'Two body shots using both hands on the gun.'
    },
]

for drill_string in drill_strings:
    count += 1
    s = String(**drill_string)
    try:
        print(f"{count}: Adding '{s}' to database.")
        s.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{s}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{s}' to the database.\n{e}\n")

print(f"ADDED {added} DRILL STRING(S) TO DATABASE.")