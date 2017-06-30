from django.db import models
from common.models import Auditable
from property.models import Property

class Booking(Auditable):
    BLOCK_OFF = 0
    CANC = 1
    FULL_PAID = 2
    NON_AG = 3
    PART_PAID = 4
    PEND_APP = 5
    PEND_PAY = 6
    SUSPEND = 7
    STATES = (
        (None, 'Please select'),
        (BLOCK_OFF, 'Blocked Off'),
        (CANC, 'Cancelled'),
        (FULL_PAID, 'Fully Paid'),
        (NON_AG, 'Non Agency'),
        (PART_PAID, 'Partially Paid'),
        (PEND_APP, 'Pending Approval'),
        (PEND_PAY, 'Pending Payment'),
        (SUSPEND, 'Suspended')
    )
    state = models.IntegerField(choices=STATES, default=BLOCK_OFF)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, related_name="booking")
    from_date = models.DateField(null=True, blank=True, verbose_name='from')
    to_date = models.DateField(null=True, blank=True, verbose_name='to')
    adults = models.IntegerField(default=2)
    children = models.IntegerField(default=0, null=True)
    infants = models.IntegerField(default=0, null=True)