"""Models for the firearm scoring app.

Classes:
    Drill -- Stores details about the drill.
    FirearmType -- A list of different firearm types.
    Firearm -- Details about a firearm.
    History -- Stores the overall history.
    Score -- Stores each drill attempt and its score.
    Skill - A list of shooting skills.
    Shooter -- Details about an individual.
    String -- An individual string of a drill.
    StringParTime -- The par times of a string.
    StringDistance -- The distances of a string.
    TargetType -- Stores details about the different types of targets.
"""

__author__ = ['Joshua Schaeffer']
__version__ = '0.1.0'
__py_version__ = '3.10.6'
__creation_date__ = '2023-07-30'

from datetime import date
from django.db import models
from django.db.models import Q

class Skill(models.Model):
    """Stores the different types of shooting skills.

    Various different types of shooting skills can be associated with a drill.
    This object stores them in order to find specific drills which can improve
    those skills or to filter stats based on a type of skill.
    """

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'skill'

    def __str__(self):
        return self.name

class TargetType(models.Model):
    """A collection of the different types of targets.

    There are numerous different types of targets available to shooters and
    drills often require a specific type of target. This object is a collection
    of the different types of targets, their attributes, and where to purchase
    them.
    """

    TARGET_COLORS = [
        (0, 'No Color/Standard'),
        (1, 'Black'),
        (2, 'Orange'),
        (3, 'Blue'),
        (4, 'Green'),
        (5, 'Red'),
        (9, 'Other'),
    ]

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=64, blank=True)
    color = models.PositiveSmallIntegerField(choices=TARGET_COLORS, default=0)
    target_url_1 = models.URLField(max_length=255, blank=True)
    target_url_2 = models.URLField(max_length=255, blank=True)
    target_url_3 = models.URLField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='target_images/', blank=True)

    class Meta:
        db_table = 'target_type'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'version', 'color'],
                name='unique_target_name_version_color'
            )
        ]

    def __str__(self):
        return self.name

class FirearmType(models.Model):
    """A list of firearm types.

    This object includes firearm types to easily identify a score based on
    type.
    """

    type = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'firearm_type'
    
    def __str__(self):
        return self.type

class Firearm(models.Model):
    """The firearm used by the shooter to perform a drill.
    
    A simple object that stores the name of firearms that the shooter can use
    to perform the drill.
    """
    
    model = models.CharField(max_length=128, unique=True)
    make = models.CharField(max_length=128)
    type = models.ForeignKey(FirearmType, on_delete=models.PROTECT)
    caliber = models.CharField(max_length=64, blank=True)
    sight_type = models.CharField(max_length=64, blank=True, null=True)
    barrel_length = models.IntegerField(blank=True, null=True)
    suppressed = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'firearm'

    def __str__(self):
        return f'{self.manufacturer} {self.model}'

class Drill(models.Model):
    """Drill information.

    A drill is a shooting exercise which consists of one or more strings. The
    details of the individual string are stored in the `String` object. All the
    strings of a drill constitue specific steps unique to each drill. In order
    to execute the drill, the shooter must perform all the steps of each string
    to the best of their ability. Drills are designed to teach a wide range of
    shooting skills and to help the shooter improve those skills. This object
    stores the details of an entire drill, what skills it focuses on, and how
    it is setup and executed. Drills are often timed and scored, although this
    is not required. How a drill is scored varies between drills and is
    described in the details of each drill.
    """

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    targets = models.ManyToManyField(TargetType)
    skills = models.ManyToManyField(Skill)
    scoring_description = models.TextField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'drill'

    def __str__(self):
        return self.name

class String(models.Model):
    """A specific event or set of events that is part of a drill.

    A string is an individual component of a drill. Some drills have multiple
    strings while others only have one. Strings are typically delinated between
    each other by a timed action, however this is not always the case. The
    shooter will perform some set of steps and may be timed. This might be
    repeated multiple times and/or in different ways to perform the entire
    drill.
    """

    drill = models.ForeignKey(Drill, on_delete=models.PROTECT)
    seqno = models.IntegerField(default=1)
    live_round_count = models.PositiveIntegerField(default=0)
    dummy_round_count = models.PositiveIntegerField(default=0)
    instructions = models.TextField()

    class Meta:
        db_table = 'drill_string'
        constraints = [
            models.UniqueConstraint(
                fields=['drill', 'seqno'], name='unique_drill_seqno'
            )
        ]

    def __str__(self):
        return f'{self.drill.name} string #{self.seqno}'

class StringParTime(models.Model):
    """A list of par times for a particular drill string.

    Drill strings can have different par times for the same string or for
    various levels of proficiency.
    """

    string = models.ForeignKey(String, on_delete=models.PROTECT)
    par = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True
    )
    firearm_type = models.ForeignKey(
        FirearmType, on_delete=models.PROTECT, blank=True, null=True
    )
    note = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'drill_string_par'
        constraints = [
            models.UniqueConstraint(
                fields=['string', 'par', 'firearm_type'],
                name='unique_string_with_par_and_type'
            ),
            models.UniqueConstraint(
                fields=['string', 'par'],
                condition=Q(firearm_type=None),
                name='unique_string_with_par_and_no_type'
            ),
            models.UniqueConstraint(
                fields=['string', 'firearm_type'],
                condition=Q(par=None),
                name='unique_string_with_no_par_and_type'
            ),
            models.UniqueConstraint(
                fields=['string'],
                condition=Q(par=None) & Q(firearm_type=None),
                name='unique_string_with_no_par_and_no_type'
            ),
        ]
    
    def __str__(self):
        return f'{self.string.drill.name} string #{self.string.seqno} par time: {self.par}'

class StringDistance(models.Model):
    """The distance for a particular drill string.

    Drill strings can have different distances for the same string.
    """

    DISTANCE_TYPES = [
        (0, 'Yards'),
        (1, 'Feet'),
        (2, 'Meters'),
    ]

    string = models.ForeignKey(String, on_delete=models.PROTECT)
    starting_distance = models.PositiveIntegerField(blank=True)
    ending_distance = models.PositiveIntegerField(blank=True, null=True)
    distance_type = models.PositiveSmallIntegerField(
        choices=DISTANCE_TYPES, blank=True, default=0
    )

    class Meta:
        db_table = 'drill_string_distance'
        constraints = [
            models.UniqueConstraint(
                fields=['string', 'starting_distance', 'distance_type'],
                name='unique_string_distance'
            )
        ]
    
    def __str__(self):
        return f'{self.string.drill.name} string #{self.string.seqno} distance: {self.starting_distance}'

class Shooter(models.Model):
    """The details of the shooter performing a drill.

    A shooter is the individual performing/attempting the drill to record and
    improve their skills.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'shooter'

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.last_name else f'{self.first_name}'

class Score(models.Model):
    """Stores each attempt of a drill.

    The `Score` object stores each attempt of a drill by a shooter and records
    all the details of that attempt. Even if a drill does not have a calculated
    score it should be recorded. The score is used to determine the level of
    proficiency or a baseline of how well the shooter does for a particular
    drill.
    """
    
    drill = models.ForeignKey(Drill, on_delete=models.PROTECT)
    string = models.ForeignKey(String, on_delete=models.PROTECT)
    shooter = models.ForeignKey(Shooter, on_delete=models.PROTECT)
    firearm = models.ForeignKey(Firearm, on_delete=models.PROTECT)
    event_date = models.DateField(default=date.today)
    score_time = models.PositiveIntegerField(blank=True, null=True)
    generic_hits = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_1 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_2 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_3 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_4 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_5 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_6 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_7 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_8 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_9 = models.PositiveIntegerField(blank=True, null=True)
    zone_hits_10 = models.PositiveIntegerField(blank=True, null=True)
    mikes = models.PositiveIntegerField(blank=True, null=True)
    points = models.PositiveIntegerField(blank=True, null=True)
    penalties = models.PositiveIntegerField(blank=True, null=True)
    from_concealment = models.BooleanField(blank=True, null=True)
    distance = models.PositiveIntegerField(blank=True, null=True)
    headshot = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'score'

    def __str__(self):
        return str(self.id)

class History(models.Model):
    """A history of shooting events.

    Stores the date of each shooting event and the drills that were performed
    at that event.
    """

    event_date = models.DateField(default=date.today)
    drill = models.ForeignKey(Drill, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'history'
        constraints = [
            models.UniqueConstraint(
                fields=['event_date', 'drill'], name='unique_drill_event_date'
            )
        ]

    def __str__(self):
        return f'{self.event_date}: {self.drill.name}'