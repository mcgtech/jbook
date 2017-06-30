from booking.models import Booking
from django.conf import settings
from booking.filters import BookingFilter
from django_filters.views import FilterView
from braces.views import GroupRequiredMixin
from booking.tables import BookingTable
from django_tables2 import SingleTableView
from django.http import HttpResponse
from common.views import get_query_by_key


# for code that does the filtering (using django-filter) see /Users/stephenmcgonigal/django_projs/client/filters.py
# https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
# https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html
# https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
# https://django-filter.readthedocs.io/en/develop/guide/usage.html#the-template
# restrict access: # https://github.com/brack3t/django-braces & http://django-braces.readthedocs.io/en/v1.4.0/access.html#loginrequiredmixin
class BookingViewFilter(GroupRequiredMixin, FilterView, SingleTableView):
    group_required = [settings.BO_GROUP, settings.ADMIN_GROUP]
    model = Booking
    table_class = BookingTable # /Users/stephenmcgonigal/django_projs/client/tables.py
    filterset_class = BookingFilter # see /Users/stephenmcgonigal/django_projs/client/filters.py
    template_name='booking_search.html'
    # see /Users/stephenmcgonigal/django_projs/cmenv/lib/python3.5/site-packages/django_tables2/client.py
    # SingleTableMixin class (SingleTableView inherits from it)
    table_pagination = {'per_page': 5}
    context_table_name = 'booking_table'
