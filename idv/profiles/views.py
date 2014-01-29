from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#from .forms import LoginForm
from django.views.generic import DetailView, UpdateView, CreateView
from .models import Profiel

class ProfielView(DetailView):
    template_name='profiel.html'
    context_object_name='profiel'
    success_url='profiel'

    def get_object(self):
        return self.request.user.profiel

    #model = Profiel
    #slug_field = 'user'
    #queryset = Profiel.objects.get(username=self.request.user.username)
    #def get_queryset(self):
    #    return Profiel.objects.get(user=self.request.user)
        #publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
        #return Book.objects.filter(publisher=publisher)


class ProfielAanpassenView(UpdateView):
    template_name='profielaanpassen.html'
    context_object_name='profiel'

    def get_object(self):
        return self.request.user.profiel


class RegistrerenView(CreateView):
    template_name='registreren.html'
    model=Profiel


@login_required
def profiel(request):
    return HttpResponse("Hello %s" % request.user.email)


def inloggen(request):
    return render(request, 'inloggen.html', {'form': LoginForm()})
    #return HttpResponse("Inloggen")


@login_required
def uitloggen(request):
    logout(request)
    return redirect('home')
