from booking.models import Booking
import django_filters
from django.db.models import Q

class BookingFilter(django_filters.FilterSet):
    adults = django_filters.CharFilter(lookup_expr='icontains')
    state = django_filters.ChoiceFilter(choices=Booking.STATES, label='State')
    class Meta:
        model = Booking
        fields = ['adults', 'state']