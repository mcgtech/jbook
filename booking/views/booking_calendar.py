from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar, monthrange
from datetime import datetime, date, timedelta
from booking.models import Booking
from django.shortcuts import render
from property.models import Property
import dateutil.parser
import calendar
import dateutil.parser

def booking_calendar(request, prop_id, pYear, pMonth):
    """
    Show calendar of events for specified month and year
    """
    prop = Property.objects.get(pk=prop_id)
    prop_start_day = prop.get_start_day_index_for_calendar()
    lYear = int(pYear)
    lMonth = int(pMonth)
    my_bookings = get_bookings_for_avail_cal(lYear, lMonth)
    lCalendar = BookingCalendar(my_bookings, prop_start_day).formatmonth(lYear, lMonth)
    lPreviousYear = lYear
    lPreviousMonth = lMonth - 1
    if lPreviousMonth == 0:
        lPreviousMonth = 12
        lPreviousYear = lYear - 1
    lNextYear = lYear
    lNextMonth = lMonth + 1
    if lNextMonth == 13:
        lNextMonth = 1
        lNextYear = lYear + 1
    lYearAfterThis = lYear + 1
    lYearBeforeThis = lYear - 1
    lToday = datetime.now()

    return render(request, 'booking_calendar.html', {'Calendar' : mark_safe(lCalendar),
                                                       'prop_id' : prop_id,
                                                       'Month' : lMonth,
                                                       'MonthName' : named_month(lMonth),
                                                       'curr_year' : lToday.year,
                                                       'curr_month' : lToday.month,
                                                       'Year' : lYear,
                                                       'PreviousMonth' : lPreviousMonth,
                                                       'PreviousMonthName' : named_month(lPreviousMonth),
                                                       'PreviousYear' : lPreviousYear,
                                                       'NextMonth' : lNextMonth,
                                                       'NextMonthName' : named_month(lNextMonth),
                                                       'NextYear' : lNextYear,
                                                       'YearBeforeThis' : lYearBeforeThis,
                                                       'YearAfterThis' : lYearAfterThis,
                                                   })


def get_bookings_for_avail_cal(lYear, lMonth):
    # https://stackoverflow.com/questions/36155332/how-to-get-the-first-day-and-last-day-of-current-month-in-python
    _, num_days = calendar.monthrange(lYear, lMonth)
    first_day = dateutil.parser.parse(str(lYear) + '-' + str(lMonth) + '-01')
    last_day = dateutil.parser.parse(str(lYear) + '-' + str(lMonth) + '-' + str(num_days))
    # 6 days either side so we can do the shoulder days
    from_date = first_day - timedelta(days=6)
    to_date = last_day + timedelta(days=6)
    my_bookings = Booking.get_bookings_in_range(from_date, to_date, True)
    return my_bookings


# http://drumcoder.co.uk/blog/2010/jun/13/monthly-calendar-django/
class BookingCalendar(HTMLCalendar):

    def __init__(self, bookings, start_day):
        super(BookingCalendar, self).__init__(start_day)
        self.bookings = self.group_by_day(bookings)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            lToday = datetime.now().date()
            if lToday == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.bookings:
                cssclass += ' filled'
                body = []
                for booking in self.bookings[day]:
                    body.append('<a href="%s">' % booking.get_absolute_url())
                    body.append('xxx')
                    body.append('</a><br/>')
                return self.day_cell(cssclass, '<div class="dayNumber">%d</div> %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, '<div class="dayNumber">%d</div>' % day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(BookingCalendar, self).formatmonth(year, month)

    def group_by_day(self, bookings):
        # for booking in bookings:
        #     print(booking.from_date)
        field = lambda booking: booking.from_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(bookings, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

from calendar import monthrange

def named_month(pMonthNumber):
    """
    Return the name of the month, given the month number
    """
    return date(1900, pMonthNumber, 1).strftime('%B')
