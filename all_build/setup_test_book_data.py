from property.models import Property
from booking.models import Booking
from datetime import datetime
from django.contrib.auth.models import User
import dateutil.parser

prop = Property.objects.get(code='A902')
admin = User.objects.get(pk=1)

Booking.objects.all().delete()
book = Booking()
book.created_by = admin
book.modified_by = admin
book.created_on = datetime.now()
book.modified_on = datetime.now()
book.property = prop
book.from_date = '2017-06-16'
book.to_date = '2017-06-23'
book.save()

book = Booking()
book.created_by = admin
book.modified_by = admin
book.created_on = datetime.now()
book.modified_on = datetime.now()
book.property = prop
book.from_date = '2017-06-30'
book.to_date = '2017-07-07'
book.save()

book = Booking()
book.created_by = admin
book.modified_by = admin
book.created_on = datetime.now()
book.modified_on = datetime.now()
book.property = prop
book.from_date = '2017-07-21'
book.to_date = '2017-07-28'
book.save()