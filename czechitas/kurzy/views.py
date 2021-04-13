from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models

class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')

class KurzyView(ListView):
    model = models.Kurzy
    template_name = "kurzy/kurzy.list.html"
