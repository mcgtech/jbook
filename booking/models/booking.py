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

    class Meta:
        ordering = ('from_date', ) # ascending from date order

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('booking_edit', args=[str(self.id)])

    @staticmethod
    def get_bookings_in_range(from_date, to_date, include_cancelled):
        bookings = Booking.objects.filter(from_date__gte=from_date, from_date__lte=to_date,)
        if include_cancelled == False:
            bookings = bookings.filter(state!=CANC)
        return bookings
