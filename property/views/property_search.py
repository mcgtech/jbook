from django.contrib.auth.decorators import login_required, user_passes_test
from common.views import *
from property.models import Property

@login_required
@user_passes_test(back_office_user, 'jbook_login')
def property_search(request):
    # I use js datatables to provide client side searching of properties
    # this involves generating a table of the properties on the server, sending to the browsres
    # then using https://datatables.net to filter and sort
    # if this becomes slow, then look at using django-tables2 & django-filters - see booking search for example
    # of this
    properties = Property.objects.all()
    return render(request, 'property_search.html', {'properties': properties,})