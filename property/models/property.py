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
    type = models.IntegerField(choices=TYPES, default=None)
    name = models.CharField(max_length=100, blank=True)