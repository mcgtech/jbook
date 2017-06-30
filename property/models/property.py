from django.db import models
from common.models import Auditable

class Property(Auditable):
    CAST = 0
    COTT = 1
    LAHS = 2
    TYPES = (
        (None, 'Please select'),
        (CAST, 'Castle'),
        (COTT, 'Cottage'),
        (LAHS, 'Large House')
    )
    SUN = 0 # ties in with js
    MON = 1
    TUE = 2
    WED = 3
    THR = 4
    FRI = 5
    SAT = 6
    DAYS = (
        (None, 'Please select'),
        (SUN, 'Sunday'),
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THR, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
    )
    ALL_YEAR = 0
    OFF_LOW_MED = 1
    OFF_LOW = 2
    WILL_CON = 3
    BASIC = 4
    BOOK_RULES = (
        (None, 'Please select'),
        (ALL_YEAR, 'All Year'),
        (OFF_LOW_MED, 'Off, Low, Medium'),
        (OFF_LOW, 'Off, Low'),
        (WILL_CON, 'Will Consider'),
        (BASIC, 'Basic')
    )
    type = models.IntegerField(choices=TYPES, default=None)
    name = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=20)
    start_day = models.IntegerField(choices=DAYS, default=None)
    booking_rule = models.IntegerField(choices=BOOK_RULES, default=None)
    promotion = models.TextField(default=None)
    short_description = models.TextField(default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name + ' (' + self.code + ')'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('property_edit', args=[str(self.id)])