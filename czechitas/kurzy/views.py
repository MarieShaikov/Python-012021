from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


from django.views.generic.base import TemplateView

from . import models

class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')

class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy.list.html"

from django.views.generic import ListView, DetailView, CreateView

class VytvorPrihlasku(CreateView):
    model = models.Prihlaska
    template_name = "prihlaska/prihlaska.html"
    fields = ["email", "jmeno", "prijmeni", "motivace", "kurz"]
    success_url = reverse_lazy('potvrzeni_prihlasky')

class PotvrzeniPrihlasky(TemplateView):
    template_name = "prihlaska/potvrzeni.html"