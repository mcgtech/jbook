from booking.models import Booking
from django_tables2 import tables, LinkColumn, A, Column

class BookingTable(tables.Table):
    # https://stackoverflow.com/questions/33184108/how-to-change-display-text-in-django-tables-2-link-column
    # http://django-tables2.readthedocs.io/en/latest/pages/api-reference.html#linkcolumn
    booking_id = LinkColumn('booking_edit', text=lambda record: record.id, args=[A('pk')], attrs={'a': {'target': '_blank'}})

    class Meta:
        model = Booking
        # fields to display in table
        fields = ('property',)
        attrs = {"class": "paleblue table table-striped table-hover table-bordered"}
        sequence = ('booking_id', '...',)