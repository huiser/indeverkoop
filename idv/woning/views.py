from django.views.generic import ListView
from .models import Woning

class WoningList(ListView):
    model = Woning

