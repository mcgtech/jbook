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

# TODO: tidy up variable names
def booking_calendar(request, prop_id, pYear, pMonth):
    """
    Show calendar of events for specified month and year
    """
    prop = Property.objects.get(pk=prop_id)
    prop_start_day = prop.get_start_day_index_for_calendar()
    lYear = int(pYear)
    lMonth = int(pMonth)
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
    first_day = dateutil.parser.parse(str(lYear) + '-' + str(lMonth) + '-01')
    total_pre_month_shoulder_days = get_total_pre_month_shoulder_days(first_day, prop_start_day)
    shoulder_days = 6
    _, num_days = calendar.monthrange(lYear, lMonth)
    _, prev_month_num_days = calendar.monthrange(lPreviousYear, lPreviousMonth)
    my_bookings = get_bookings_for_avail_cal(lYear, lMonth, shoulder_days, num_days, first_day)
    lCalendar = BookingCalendar(my_bookings, prop_start_day, lYear, lMonth, prev_month_num_days,
                                total_pre_month_shoulder_days, lPreviousMonth, lNextMonth).formatmonth(lYear, lMonth)
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


def get_bookings_for_avail_cal(lYear, lMonth, shoulder_days, num_days_in_month, first_day):
    # https://stackoverflow.com/questions/36155332/how-to-get-the-first-day-and-last-day-of-current-month-in-python
    last_day = dateutil.parser.parse(str(lYear) + '-' + str(lMonth) + '-' + str(num_days_in_month))
    # 6 days either side so we can do the shoulder days
    from_date = first_day - timedelta(days=shoulder_days)
    to_date = last_day + timedelta(days=shoulder_days)
    my_bookings = Booking.get_bookings_in_range(from_date, to_date, True)
    return my_bookings
#
# def get_prev_month(curr_month):
#     if curr_month == 1:
#         return 12
#     else:
#         return curr_month - 1
#
# def get_next_month(curr_month):
#     if curr_month == 12:
#         return 1
#     else:
#         return curr_month + 1

def get_total_pre_month_shoulder_days(first_day_of_month, prop_start_day):
    d = first_day_of_month
    delta = timedelta(days=1)
    count = 0
    while d.weekday() != prop_start_day:
        d = d - delta
        count = count + 1
    return count - 1

def get_bookings_cell_markup(month_data, day, cssclass):
    markup = ''
    if day in month_data:
        cssclass += ' filled'
        body = []
        for booking in month_data[day]:
            body.append('<a href="%s">' % booking.get_absolute_url())
            body.append(booking.get_date_range_str())
            body.append('</a><br/>')
        markup = ''.join(body)

    return cssclass, markup


# http://drumcoder.co.uk/blog/2010/jun/13/monthly-calendar-django/
class BookingCalendar(HTMLCalendar):

    def __init__(self, bookings, start_day, lYear, lMonth, prev_month_num_days, total_pre_month_shoulder_days, lPreviousMonth, lNextMonth):
        super(BookingCalendar, self).__init__(start_day)
        self.bookings = self.group_by_day(bookings, lYear, lMonth, lPreviousMonth, lNextMonth)
        self.curr_month_dates_started = False
        self.next_month_day = 0
        self.prev_month_day = prev_month_num_days - total_pre_month_shoulder_days - 1
        self.prev_month = lPreviousMonth
        self.next_month = lNextMonth

    def formatday(self, day, weekday):
        day_cell = None
        if day == 0:
            cssclass = 'noday'
            if self.curr_month_dates_started:
                # we are now processing days after current month
                self.next_month_day = self.next_month_day + 1
                day = self.next_month_day
                _, cell_markup = get_bookings_cell_markup(self.bookings[self.next_month], day, cssclass)
            else:
                # we are processing shoulder days for previous month
                self.prev_month_day = self.prev_month_day + 1
                day = self.prev_month_day
                _, cell_markup = get_bookings_cell_markup(self.bookings[self.prev_month], day, cssclass)
        else:
            self.curr_month_dates_started = True
            cssclass = self.cssclasses[weekday]
            lToday = datetime.now().date()
            if lToday == date(self.year, self.month, day):
                cssclass += ' today'
            cssclass, cell_markup = get_bookings_cell_markup(self.bookings[self.month], day, cssclass)
        return self.day_cell(cssclass, '<div class="dayNumber">%d</div> %s' % (day, cell_markup))

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(BookingCalendar, self).formatmonth(year, month)

    def group_by_day(self, bookings, lYear, lMonth, lPreviousMonth, lNextMonth):
        month_dates = {lPreviousMonth : {}, lMonth : {}, lNextMonth: {}}
        delta = timedelta(days=1)
        for booking in bookings:
            d = booking.from_date
            while d <= booking.to_date:
                if d.day not in month_dates[d.month]:
                    month_dates[d.month][d.day] = []
                month_dates[d.month][d.day].append(booking)
                d = d + delta
        return month_dates
        # field = lambda booking: booking.from_date.day
        # return dict(
        #     [(day, list(items)) for day, items in groupby(bookings, field)]
        # )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

from calendar import monthrange

def named_month(pMonthNumber):
    """
    Return the name of the month, given the month number
    """
    return date(1900, pMonthNumber, 1).strftime('%B')
