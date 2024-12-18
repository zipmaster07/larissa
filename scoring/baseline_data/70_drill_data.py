"""Populates the database with the `Drill` object data."""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-08-03'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larissa.settings')

import django
django.setup()

from django.db.utils import IntegrityError
from scoring.models import Drill, Skill, TargetType

count = 0
added = 0
print('ADDING DRILLS TO DATABASE...')
drills = [
    {
        'name': '2x2x2',
        'description': 'The Viking Tactics rifle (or carbine) drill developed by Kyle Lamb is a simple exercise. Nicknamed the 2x2x2 drill, it is designed to build speed and accuracy when engaging multiple targets. The scenario: You suddenly encounter three bad guys at close range and must deal with them quickly with your AR-15 or sidearm.',
        'scored': True,
        'scoring_description': 'Scoring uses the standard Bill Drill scoring mechanism. A simple hit factor is calculated by multiplying each zone hit by a score (see below), adding all the zone hits together and dividing by the total time.\n\n- A zone = 5 points\n- C zone = 3 points\n- D zone = 1 point\n- Mike = 0 points\n\nFor example, out of 6 shots, 5x “A zone” hits and 1x “C zone” hit in 2.5 seconds would be: (5 * 5) + (3 * 1) / 2.5 = 11.2.',
        'notes': '',
    },
    {
        'name': '3M',
        'description': 'Developed by Tom Givens. This drill tests movement off the line of force, a rapid presentation from concealment, accurate placement of multiple fast shots, a malfunction remedy, a precise head shot, and an empty gun reload, all under time pressure. It only requires 10 rounds, one target, and a timer or stopwatch to test/measure all of these skills.',
        'scored': True,
        'scoring_description': 'Shooter must move on the draw, move on the malfunction, and move on the reload. Failing to move for any manipulation is a 5 point penalty. If doing pass/fail, any round outside the highest value zone is a failure.\n\nComstock Count Scoring:\n- 45 possible points out of 9 shots. You can adjust the scoring as desired.\n- Standard points are:\n\t- A zone = 5 points\n\t- C zone = 3 points\n\t- D zone = 2 points\n\t- Mike = 0 points\n- Points / Time = Index\n- Index * 30 = Score\n- Example: 42 points, fired in 12.15 seconds would be a score of 103.8:\n\t- 42 / 12.15 = 3.46\n\t- 3.46 * 30 = 103.8\n\t- Score = 103.8\n- Par Score = 75, anything over 100 is very good work. Anything over 125 is extremely high skill.\n\nOn Pass/Fail scoring, shooter fails if he/she:\n- Does not move on the draw, the malfunction, and the reload.\n- Does not tap the magazine before running the slide on the malfunction.\n- Places a single hit outside the highest scoring zone on the target.\n- Is over the time limit.',
        'notes': 'As you improve, adjust the scoring. For example, lower the amount of points received from non-a-zone hits, have a penalty for misses, etc.',
    },
    {
        'name': '5x5',
        'description': "This is a great exercise to get a baseline of where your overall skill level is or you can use it to find out how you're doing with a particular gun. Originated by Gila Hayes in her book and then Claude Werner added some repetitions. Goal is to get all five rounds inside the 5 inch circle within 5 seconds.",
        'scored': True,
        'scoring_description': 'This drill is a pass/fail drill. A pass is 25 shots with no misses. While the entire drill is pass/fail it is useful to show progress by keeping track of how many hits and misses the shooter has. A score can be kept by assigning 1 point per hit. A score of 25 would be a pass, anything less would be a fail.',
        'notes': '',
    },
    {
        'name': '9-Hole',
        'description': "Designed by Vikings Tactics and using their VTAC barricade, this drill gives shooters an easy, range-­worthy, training tool that can be used frequently to help develop the ability to return fire from awkward, nonstandard positions.",
        'scored': True,
        'scoring_description': 'This drill is scored slightly differently depending on the type of target used. For steel a hit factor is calculated by dividing the total number of shots by the total time and multiplying by 100. For paper targets the hit factor is calculated by dividing the total number of hits by the total time and multiplying by 100. For steel targets a lower hit factor is better while for paper targets a higher hit factor is better.\nFor example when using steel if the total number of shots was 9 with a time of 65.41, then the score would be (9 / 65.41) * 100 = 13.76.\nFor a paper target if the shooter got 6 hits in 70.11 seconds then the score would be (6 / 70.11) * 100 = 8.56\n',
        'notes': '',
    },
    {
        'name': 'Active Shooter',
        'description': "Designed to simulate a stressful environment in a potential active killer situation, this drill involves running as fast as possible while carrying weight and then shooting from cover to eliminate a threat. The drill will require a duffle bag or similar weighted down to about 60 lbs and a barricade (a table, barrel, dedicated barricade, etc). Sand or water can be used as the weights. The total weight can be adjusted for the shooter, situation, and the desired level of difficulty. The shooter will pick up the duffle bag as if needing to help or carry a small person or object during an active killer situation.",
        'scored': True,
        'scoring_description': 'A simple hit factor is calculated by multiplying each zone hit by a score (see below), adding all the zone hits together and dividing by the total time. This hit factor is then multiplied by 50.\n\n- A zone = 5 points\n- C zone = 3 points\n- D zone = 1 point\n- Mike = 0 points\n\nSubtract the best hit(s) for any shots outside of par, regardless of where those shots landed.\n\nFor example, out of 5 shots, 3x “A zone” hits, 1x “C zone” hit, and 1x “Mike” in 13.21 seconds, where the last shot was outside of par would be:\n- For A zone hits: 5 * 2 = 10 (One of the A zone hits is disqualified because of the shot outside of par).\n- For C zone hits: 3 * 1 = 3\n- For Mikes: 0 * 2 = 0 (The shot outside of par counts as a Mike).\n- Hit factor: (10 + 3 + 0) / 13.21 = 0.98\n- Score: 0.98 * 50 = 49',
        'notes': 'After becoming comfortable and confident in the drill, try increasing the weight or forcing the shooter to shoot the target at an angle.',
    },
    {
        'name': 'Bill Drill',
        'description': 'Originally designed by Bill Wilson. Goal is to have all six shots in the down zero (A zone). This helps working on establishing grip on the draw, seeing just enough of what you need to see, but not over confirming and then running the trigger well at speed with recoil management. This drill is best done “cold” as it is a measure of actual performance.',
        'scored': True,
        'scoring_description': 'A simple hit factor is calculated by multiplying each zone hit by a score (see below), adding all the zone hits together and dividing by the total time.\n\n- A zone = 5 points\n- C zone = 3 points\n- D zone = 1 point\n- Mike = 0 points\n-nFor example, out of 6 shots, 4x “A zone” hits, 1x “C zone” hit, and 1x “D zone” hit in 4 seconds would be: ((5 * 4) + (3 * 1) + (1 * 1)) / 4 = 6. Penalties: Add 0.5 seconds for each shot after par',
        'notes': '',
    },
    {
        'name': 'Bright Light',
        'description': 'A night pistol drill to help test quick/positive identification of a target, it requires a flashlight and at least two targets (although easier versions can use one). The final form of this drill is meant to be used with a hostage style target, however any body style target (IPSC, IDPA, etc) can be used when learning the drill. The drill is meant to be performed at night (again, can be performed during the day to make it easier). Two target stands should be set up, but only one of them should have the printed target on it, the other should be blank. It is best to have someone else set up the targets without the shooter knowing which one he/she will shoot (this may not always be possible).',
        'scored': True,
        'scoring_description': 'This drill is pass/fail. To pass the drill the shooter must ID both targets and all five shots must make contact with the threat within par. Any shots outside of par, shots off paper, shots that make contact with the hostage, or failure to shine the light on both targets is considered a drill failure. While the drill is pass/fail it is best to record key data such as time, hits on target, missed hits, hits on the hostage, etc.',
        'notes': 'For newer shooters or even those that are just new to the drill itself, several steps can be removed or replaced to make the drill easier such as the 180° turn, using a non-hostage target, or using only one target to start.',
    },
    {
        'name': 'Cadence Drill',
        'description': 'Developed by T.REX Arms this drill is designed to improve the rhythm and cadence of shots.',
        'scored': True,
        'scoring_description': 'This drill is to work on a balance of speed and accuracy. Rather than counting in your head when shooting the target, shoot as fast as you can keep rounds inside the circles. On the smaller circles, cadence will slow down. Try to maintain consistency. You’ll want your splits to be something like… .30, .31, .30, .32, etc. Not: .32, .37, .34, .43. Use a shot timer to record your splits by hitting the timer and waiting a second or two and begin the string of fire.',
        'notes': '',
    },
    {
        'name': 'Casino',
        'description': 'Created by Tom Givens. This drill is a great way to practice almost all of the most important defensive shooting skills with less than half a box of ammo.',
        'scored': True,
        'scoring_description': 'Scoring is based on the total hits (called points), divided by time, times 100. Add one second to total time for each miss and for each shot fired out of sequence or other procedural error. A “perfect” score is 21 hits in 21 seconds which would be a score of 100. Under 100 would mean either less than 21 hits or over 21 seconds (or both). Over 100 means all 21 hits in under 21 seconds.\n\nFor example 19 hits in 22 seconds is a score of 79.2:\n- 19 hits out of 21 possible = 2 misses.\n- Total time was 22 seconds then add 2 seconds to the total time, 1 second per miss: 24 seconds.\n- 19 / 24 = 0.7916\n- 0.7916 * 100 = 79.2 (rounded)',
        'notes': 'You can purchase alternate targets to change up the positions and presentation of the target shapes. Also, load your magazines differently. Load one mag with 6 rounds, one with 7 rounds, and one with 8 rounds. Or have someone else load your magazines with a random number of rounds as long as it equates to 21 total rounds.',
    },
    {
        'name': 'Check Down',
        'description': 'This drill has been around since the early 2000’s by Mid-South/Shaw Shooting. This drill helps you train when your rifle goes down in a CQB situation to transition to your pistol. ',
        'scored': False,
        'scoring_description': 'Although hits are tracked, this drill is not necessarily scored. What is more important is time intervals. What should be tracked is\n- Time to first shot.\n- Time between first rifle and first pistol shot.\n- Time between pistol shot and rifle reload and second shot.\n- Zone hits',
        'notes': 'When transitioning from rifle to pistol, make sure the rifle does not get bound up by your sling. A good tip is to slide your support hand along the handrail back to the magazine and then briskly, but under control, place the rifle at your side. Simultaneously move your strong hand to your pistol to begin your draw.',
    },
    {
        'name': 'Cold Start',
        'description': 'This drill is intended to be shot "cold" meaning, first rounds down range without any warmup. This is a pass or fail drill, focusing on "on-demand" performance, accuracy, shooting while moving, single handed shooting, and reloading. From Tier 1 Concealed.',
        'scored': True,
        'scoring_description': 'Scoring is pass/fail. All rounds must hit their respective targets to pass in or under the par time set. Failure to move or not shoot with your dominant/support hand when you are supposed to is a failure.',
        'notes': 'Focus on consistent movement and splits while engaging the center target. You should not be rushing to the 3 yard and then taking shots.',
    },
    {
        'name': 'Collateral',
        'description': 'Taken from the movie “Collateral” the drill is a close range, drawn from holster, pistol drill. Essentially and extended or modified Mozambique, you will need two targets spaced about 4 - 6 feet apart from each other.',
        'scored': True,
        'scoring_description': 'A simple hit factor is calculated by multiplying each zone hit by a score (see below), adding all the zone hits together and dividing by the total time.\n\nA zone = 5 points\nC zone = 3 points\nD zone = 1 point\nMike = -1 points\n\nFor example, out of 5 shots, 2x “A zone” hits, 1x “C zone” hit, and 1x “D zone” hit in 2.5 seconds would be: ((5 * 2) + (3 * 1) + (1 * 1)) / 2.5 = 5.6.\n\nPenalties: Add 0.5 seconds for each shot after par.',
        'notes': 'The drill can be slightly modified by shooting the very last shot into the headshot A zone. ',
    },
    {
        'name': "Cornucopia",
        'description': 'This 50 round pistol course emphasizes a balance of speed and marksmanship while reinforcing both fundamental and advanced skills, such as movement and target transitions. Great for comparing yourself against different handguns, loadouts, or a friend. You will need 50 rounds of ammunition, 3 USPSA style targets, and 20 meters of usable space.',
        'scored': True,
        'scoring_description': 'The score is calculated by adding the total points received between all three targets divided by the total time taken for all 8 strings. The left target should have 2 head shots and 15 torso shots, the middle target should have 2 head shots and 13 torso shots, and the right target should have 2 head shots and 16 torso shots. The left and right targets can be swapped depending on how the shooter executes the fourth string. Instead of going from center, to left, to right, back to center, the shooter may go center, to right, to left, back to center. Simply swap the two target’s values if this occurs.\n\nTo calculate the score, tally all of the hits in each zone for each target and multiply each zone by the score below:\n- A zone = 5 points\n- C zone = 3 points\n- D zone = 0 points\n- Mike = -10 points\n\nNext, take the sum of each string to get the total time and then divide the total points by your total time to get your hit factor. For example:\n- Left target: 12x “A zone” hits, 2x “C zone” hits, and 1x “D zone” hit.\n- Middle target: 14x “A zone” hits, 1x “D zone” hit.\n- Right target: 11x “A zone hits”, 6x “C zone” hits, 1x Mike.\n- Sum of all 8 strings: 78.25 seconds\n\nThe total points would be:\n- For “A zone” hits: (12 + 14 + 11) * 5 = 185\n- For “C zone” hits: (2 + 6) * 3 = 24\n- For “D zone” hits: (1 + 1) * 0 = 0\n- For Mikes: 1 * -10 = -10\n- Total points = 185 + 24 + 0 + (-10) = 199\n\nThe hit factor would be: 199 / 78.25 = 2.54',
        'notes': 'You can vary the drill by changing up certain parameters or situations, e.g.., only using one hand throughout or use weak hand, more required headshots, introduce more malfunctions, require emergency reloads, etc.\nWhen first starting out, focus on hits more than time. After you become comfortable with the drill try to incrementally reduce your time.',
    },
    {
        'name': 'Dot Torture',
        'description': 'Dot Torture is one of the best pistol drills out there for working on your trigger control -- a skill almost all shooters could stand to improve. Developed by David Blinder, popularized by Todd L. Green. Goal is to shoot it clean consistently at the recommended distance and then move a yard back. Shoot it clean consistently again and continue to move further back.',
        'scored': True,
        'scoring_description': 'Scoring is out of 50. It is minus 1 point per miss. Hits in the wrong dot on the wrong string do not count.',
        'notes': '',
    },
    {
        'name': 'El Presidente',
        'description': 'Developed by defensive pistol-shooting pioneer, Jeff Cooper, this drill is one of the oldest combat pistol shooting drills in existence, El Prez takes all the crucial fundamentals (including speed, accuracy, a smooth draw, proper sight alignment, trigger control, and target transition) and compresses them into one beautiful package.',
        'scored': True,
        'scoring_description': 'Original scoring:\nIn its original form, this drill is a pass/fail drill. Only accurate shots count. If any of your lead falls outside the A zones, you fail the drill. Shots outside of par time can still be considered a success (depending on the shooter’s level of skill), but the ultimate goal is to shoot the drill in 10 seconds or less. If you are finding this difficult, increase the par time and make improvements from there.\n\nVirginia Count:\nThe USPSA uses El Prez as a classifier to separate shooters by skill level. The standard Virginia Count is used for scoring El Prez in competition. This scoring method takes the number of hits per target (minus any penalties) and divides that number by the total time it took the shooter to complete the drill. For scoring purposes, shots outside the A-zone do not constitute an automatic failure. Instead, different points are awarded for different zone hits. USPSA incorporates different scoring for Major and Minor caliber “power factors” that require more math than needs to be detailed here. Here’s what you need to know about scoring El Prez:\n- A-zone = 5 points\n- B- and C-zone (Major) = 4 points\n- B- and C-zone (Minor) = 3 points\n- D-zone (Major) = 2 points\n- D-zone (Minor = 1 point',
        'notes': 'Many shooters rush the second and fourth shots on each target, so it sounds like three separate double taps, a reload pause, and three more double taps to round out the drill. According to Cooper, a properly executed El Presidente will have a steady, rhythmic shot cadence. The goal should be six evenly spaced shots, a pause for the reload, and six more evenly spaced shots. This slow, deliberate rhythm is a sign the shooter is achieving a proper sight picture for each individual shot. It also indicates a smooth transition between targets. This smooth, even rhythm should be your goal when shooting El Prez.',
    },
    {
        'name': 'FBI Qualification',
        'description': "This is the FBI qualification test that all FBI agents are required to pass in order to carry a firearm on duty. While it's not necessarily an ideal tool for skill development, there are a lot of benefits for the average armed citizen to be able to demonstrate that they can pass a federally recognized shooting standard.",
        'scored': True,
        'scoring_description': 'Scoring is a percentage of hits out of all 60 rounds. A passing Score is 80% for students and 90% for instructors.',
        'notes': 'Official version of the FBI test requires the shooter to fire from behind cover on the last stage. This sometimes is difficult to set up on ranges and shouldn’t impact your overall score too much.',
    },
    {
        'name': 'First Shot',
        'description': 'A simple drill to practice drawing a sidearm from concealment and sight acquisition from close range.',
        'scored': True,
        'scoring_description': 'This drill is not scored, but rather should show a steady improvement in time and accuracy.',
        'notes': 'Once comfortable at a certain distance, move back 1 or 2 yards and repeat the drill.',
    },
    {
        'name': 'Five-yard Roundup',
        'description': 'Five yards. Four stages of fire. Two and a half seconds each. Ten rounds total. This quick and brutal shooting exercise is a great way to test your handgun skills. See the original drill description from SWAT magazine. Many individuals are practicing at longer distances or giving themselves longer timeframes that do not reflect reality of what we are actually seeing from CCTV and body cams. Developed by Justin Dyal.',
        'scored': True,
        'scoring_description': 'Scoring is based on target rings. No points for hits off the paper. Subtract 5 points for shots after the time limit.',
        'notes': 'Like most B-8 centered drills, there are levels of achievement. First, all ten hits within time on the ten-inch paper: respectable, useful, and on the right path. This equates to an approximate score of 75.\nNext, all within the eight-inch “8” ring with most in the black: solid, and demonstrating all the right stuff. This typically works out to a 90 or above score and is about what I’d look for in a SWAT or instructor-level shooter.\nNext is all in the black within time. That is usually a 95 or above and is back-slap worthy on any firing line.\nFinally, this drill is 100% max-able. The very best can do it regularly, almost on demand, but it requires that everything is done right. Often the last hit with either of the single-hand stages will frustrate that perfect run.',
    },
    {
        'name': 'Mozambique',
        'description': 'The Mozambique Drill, also known as the Failure Drill, Failure to Stop drill, or informally as “two to the body, one to the head”, is a close-quarters shooting technique that requires the shooter to fire twice into the torso of a target (known as a double tap or hammered pair to the center of mass), and follow up with a more difficult shot to the head that, if properly placed, should kill or otherwise stop the target if the previous shots failed to do so.',
        'scored': False,
        'scoring_description': 'This drill is typically not scored. The shooter should be trying to shoot three consistent shots with the exact same cadence for all three shots. There should be no pause between shots 2 and 3. Take your time when first shooting the drill and focus on accuracy. After some practice try to continually improve your time without sacrificing accuracy or cadence.',
        'notes': 'According to anecdotal history, the technique originated with Mike Rousseau, a Rhodesian mercenary taking part in the Mozambican War of Independence (1964–1974). While engaged in combat at the Lourenco Marques Airport in what is now Maputo, Mozambique, Rousseau rounded a corner and encountered a FRELIMO fighter armed with an AK-47 at ten paces (7.5 m (25 ft)) from his position. Rousseau fired two rounds from his Browning Hi-Power pistol into the fighter\'s upper chest, usually enough to incapacitate or kill outright; however, seeing that the fighter was still advancing, Rousseau attempted a head shot that hit the fighter through the base of his neck, severing the spinal cord and killing him. Rousseau related the story to an acquaintance, small arms expert Jeff Cooper, founder of the Gunsite Academy shooting school, who incorporated the "Mozambique Drill" into his modern technique shooting method.',
    },
    {
        'name': 'Runenation',
        'description': 'Cold start pistol or rifle drill to help warm up.',
        'scored': False,
        'scoring_description': 'This drill is a cold start drill and is not scored. Repeat the drill as many times as desired.',
        'notes': '',
    },
    {
        'name': 'Super Test',
        'description': 'Ken Hackathorn created the test. Wayne Dobbs and Darryl Bolke of Hardwired Tactical Shooting (HiTs) evolved it into the super test. Goal is to shoot a 270/300 (90%) or above. If you’re above a 290 then you are really good.',
        'scored': True,
        'scoring_description': 'Scoring is based on target rings. No points for hits off the paper or after the time limit.',
        'notes': 'For single stack pistols everything stays the same except shooting 8 rounds and a passing score is still 90% (214/240). A revolver version can be shot with 5 rounds with times of 12, 8, and 4 seconds, respectively.',
    },
    {
        'name': 'The Burger Drill',
        'description': 'This rifle drill uses two targets and focuses on grouping and firearm manipulation.',
        'scored': True,
        'scoring_description': 'Scoring is based on target rings for a total of 80 points. No points for hits off the paper or after the time limit.',
        'notes': 'Shooters can make the drill more difficult by having a friend load the two magazines with a random number of rounds so that the shooter doesn’t know when to reload. Just make sure there are a total of 8 rounds between the two magazines and that there are a minimum of 2 rounds in one of the magazines.\n\nYou can also introduce malfunctions into the drill by using dummy rounds that need to be cleared.',
    },
    {
        'name': 'Throttle Control',
        'description': 'Developed by Lucas Botkin of TRex Arms. Watch the drill here. Good drill to work basic target transitions and throttle control. All on one piece of paper.',
        'scored': True,
        'scoring_description': 'This drill is only timed. Shooters should be aiming to beat their previous time. 1 second is added for each miss.',
        'notes': 'Focus on getting good groups. Once done then you can speed up and focus on getting tight groups again.',
    },
    {
        'name': 'Wizard',
        'description': 'Developed by Ken Hackathorn. As with most good drills it seems simple on the surface, but may be a little harder than you think. Fired from a concealed-carry holster beneath a cover garment, the drill is revolver or pistol neutral, meaning it can be shot with either, there being no advantage in one over the other. You’ll need a single silhouette or Option target, a timer and only five rounds of ammunition. You can use this drill as a gut check to evaluate your current skill level by shooting it cold with your carry pistol and ammunition, or you can burn through a lot of practice ammo shooting it over and over.',
        'scored': True,
        'scoring_description': 'This drill is pass/fail. You should have three head shots and two body shots all within the time limit. Any shots off target or outside the time limit is considered a failure.',
        'notes': 'Link to original article: https://www.shootingillustrated.com/content/skills-check-the-wizard-drill/',
    },
]

for drill in drills:
    count += 1
    d = Drill(**drill)
    try:
        print(f"{count}: Adding '{d}' to database.")
        d.save()
        print()
        added += 1
    except IntegrityError as e:
        print(f"'{d}' already exists in the database, skipping.\n{e}\n")
    except Exception as e:
        print(f"Unable to add '{d}' to the database.\n{e}\n")

print('ADDING TARGETS AND SKILLS TO DRILLS...')
# 2x2x2
_2x2x2 = Drill.objects.get(name='2x2x2')
_2x2x2.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
_2x2x2.skills.add(
    Skill.objects.get(name='sight picture'),
    Skill.objects.get(name='trigger control'),
    Skill.objects.get(name='target transition')
)

# 3M
_3m = Drill.objects.get(name='3M')
_3m.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
_3m.skills.add(
    Skill.objects.get(name='marksmanship'),
    Skill.objects.get(name='movement'),
    Skill.objects.get(name='manipulation')
)

# 5x5
_5x5 = Drill.objects.get(name='5x5')
_5x5.targets.add(TargetType.objects.get(name='5x5'))
_5x5.skills.add(Skill.objects.get(name='target acquisition'))

# 9-Hole
_9hole = Drill.objects.get(name='9-Hole')
_9hole.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
_9hole.skills.add(
    Skill.objects.get(name='sight alignment'),
    Skill.objects.get(name='sight picture'),
    Skill.objects.get(name='marksmanship'),
    Skill.objects.get(name='movement'),
    Skill.objects.get(name='accuracy'),
    Skill.objects.get(name='muzzle discipline'),
    Skill.objects.get(name='stance'),
    Skill.objects.get(name='grip')
)

# Active Shooter
active_shooter = Drill.objects.get(name='Active Shooter')
active_shooter.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
active_shooter.skills.add(
    Skill.objects.get(name='fitness'),
    Skill.objects.get(name='target acquisition'),
    Skill.objects.get(name='accuracy')
)

# Bill Drill
bill_drill = Drill.objects.get(name='Bill Drill')
bill_drill.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
bill_drill.skills.add(
    Skill.objects.get(name='draw stroke'),
    Skill.objects.get(name='sight picture'),
    Skill.objects.get(name='trigger control'),
    Skill.objects.get(name='recoil management')
)

# Bright Light
bright_light = Drill.objects.get(name='Bright Light')
bright_light.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)'),
    TargetType.objects.get(name='BT-1', version=''),
    TargetType.objects.get(name='ICE-QT', version=''),
    TargetType.objects.get(name='NTC-303', version=''),
    TargetType.objects.get(name='NTC-515', version='')
)
bright_light.skills.add(
    Skill.objects.get(name='target acquisition'),
    Skill.objects.get(name='accuracy'),
)

# Cadence Drill
cadence_drill = Drill.objects.get(name='Cadence Drill')
cadence_drill.targets.add(TargetType.objects.get(name='TREX Rhythm-Cadence'))
cadence_drill.skills.add(
    Skill.objects.get(name='trigger control'),
    Skill.objects.get(name='mental discipline'),
    Skill.objects.get(name='grip'),
    Skill.objects.get(name='accuracy'),
    Skill.objects.get(name='recoil management'))

# Casino
casino = Drill.objects.get(name='Casino')
casino.targets.add(
    TargetType.objects.get(name='DT-2A'), TargetType.objects.get(name='DT-2B'),
    TargetType.objects.get(name='DT-2C')
)
casino.skills.add(
    Skill.objects.get(name='draw stroke'), Skill.objects.get(name='accuracy'),
    Skill.objects.get(name='emergency reloads')
)

# Check Down
check_down = Drill.objects.get(name='Check Down')
check_down.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)'))
check_down.skills.add(
    Skill.objects.get(name='weapons manipulation'),
    Skill.objects.get(name='reloading'),
    Skill.objects.get(name='kit shakeout')
)

# Cold Start
cold_start = Drill.objects.get(name='Cold Start')
cold_start.targets.add(TargetType.objects.get(name='T1C Cold Start'))
cold_start.skills.add(
    Skill.objects.get(name='movement'), Skill.objects.get(name='accuracy'),
    Skill.objects.get(name='emergency reloads')
)

# Collateral
collateral = Drill.objects.get(name='Collateral')
collateral.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)'),
    TargetType.objects.get(name='BT-1', version=''),
    TargetType.objects.get(name='ICE-QT', version='')
)
collateral.skills.add(
    Skill.objects.get(name='target transition'),
    Skill.objects.get(name='marksmanship'),
    Skill.objects.get(name='draw stroke')
)

# Cornucopia
cornucopia = Drill.objects.get(name="Cornucopia")
cornucopia.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
)
cornucopia.skills.add(
    Skill.objects.get(name='movement'),
    Skill.objects.get(name='target transition'),
    Skill.objects.get(name='target acquisition'),
    Skill.objects.get(name='recoil management'),
    Skill.objects.get(name='muzzle discipline'),
    Skill.objects.get(name='reloading'),
    Skill.objects.get(name='manipulation')
)

# Dot Torture
dot_torture = Drill.objects.get(name='Dot Torture')
dot_torture.targets.add(
    TargetType.objects.get(name='Pistol Dot Torture'),
    TargetType.objects.get(name='Rifle Dot Torture')
)
dot_torture.skills.add(
    Skill.objects.get(name='trigger control'),
    Skill.objects.get(name='mental discipline')
)

# El Presidente
el_presidente = Drill.objects.get(name='El Presidente')
el_presidente.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
el_presidente.skills.add(
    Skill.objects.get(name='accuracy'), Skill.objects.get(name='draw stroke'),
    Skill.objects.get(name='sight alignment'),
    Skill.objects.get(name='trigger control'),
    Skill.objects.get(name='target transition'),
    Skill.objects.get(name='cadence'),
)

# FBI Qualification
fbi_qual = Drill.objects.get(name='FBI Qualification')
fbi_qual.targets.add(TargetType.objects.get(name='IALEFI-Q'))
fbi_qual.skills.add(Skill.objects.get(name='accuracy'))

# First Shot
first_shot = Drill.objects.get(name='First Shot')
first_shot.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)'),
    TargetType.objects.get(name='B-8', version='P (paper)'),
    TargetType.objects.get(name='B-8', version='PRC (paper red center)'),
    TargetType.objects.get(name='B-8', version='T (heavy paper)')
)
first_shot.skills.add(
    Skill.objects.get(name='draw stroke'),
    Skill.objects.get(name='sight alignment')
)

# Five-yard Roundup
five_yard_roundup = Drill.objects.get(name='Five-yard Roundup')
five_yard_roundup.targets.add(
    TargetType.objects.get(name='B-8', version='P (paper)'),
    TargetType.objects.get(name='B-8', version='PRC (paper red center)'),
    TargetType.objects.get(name='B-8', version='T (heavy paper)')
)
five_yard_roundup.skills.add(Skill.objects.get(name='accuracy'))

# Mozambique
mozambique = Drill.objects.get(name='Mozambique')
mozambique.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
mozambique.skills.add(
     Skill.objects.get(name='cadence'),
     Skill.objects.get(name='accuracy'),
     Skill.objects.get(name='target transition')
)

# Runenation
runenation = Drill.objects.get(name='Runenation')
runenation.targets.add(
    TargetType.objects.get(name='Runenation Cold Start', version='')
)
runenation.skills.add(
    Skill.objects.get(name='accuracy')
)

# Super Test
super_test = Drill.objects.get(name='Super Test')
super_test.targets.add(
    TargetType.objects.get(name='B-8', version='P (paper)'),
    TargetType.objects.get(name='B-8', version='PRC (paper red center)'),
    TargetType.objects.get(name='B-8', version='T (heavy paper)')
)

# The Burger Drill
the_burger_drill = Drill.objects.get(name='The Burger Drill')
the_burger_drill.targets.add(
    TargetType.objects.get(name='B-8', version='P (paper)'),
    TargetType.objects.get(name='B-8', version='PRC (paper red center)'),
    TargetType.objects.get(name='B-8', version='T (heavy paper)')
)
the_burger_drill.skills.add(
    Skill.objects.get(name='movement'),
    Skill.objects.get(name='target transition'),
    Skill.objects.get(name='manipulation')
)

# Throttle Control
throttle_control = Drill.objects.get(name='Throttle Control')
throttle_control.targets.add(
    TargetType.objects.get(name='B-8', version='P (paper)'),
    TargetType.objects.get(name='B-8', version='PRC (paper red center)'),
    TargetType.objects.get(name='B-8', version='T (heavy paper)')
)
throttle_control.skills.add(
    Skill.objects.get(name='target transition'),
    Skill.objects.get(name='trigger control'),
    Skill.objects.get(name='recoil management')
)

# Wizard
wizard = Drill.objects.get(name='Wizard')
wizard.targets.add(
    TargetType.objects.get(name='IPSC', version='CB (cardboard)'),
    TargetType.objects.get(name='IPSC', version='P (paper)'),
    TargetType.objects.get(name='IDPA', version='CB (cardboard)'),
    TargetType.objects.get(name='IDPA', version='P (paper)')
)
wizard.skills.add(
    Skill.objects.get(name='draw stroke'),
    Skill.objects.get(name='trigger control')
)

print('ADDED TARGETS AND SKILLS TO DRILLS.')
print(f"ADDED {added} DRILL(S) TO DATABASE.")
