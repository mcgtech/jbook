
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
try:
    admin = User.objects.get(pk=1)
except:
    admin = User.objects.create_superuser('admin', 'a@a.com', 'xxx')

admin_group = Group(name="admin")
admin_group.save()