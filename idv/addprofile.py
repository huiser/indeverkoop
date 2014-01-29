from django.contrib.auth.models import User
from profiles.models import Profiel

idv=User.objects.get(username='idv')
p=Profiel(user=idv, geslacht='M')
p.save()
