from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse

class MyFirstView(View):
    def get(self, request):   #get je typ pozadavku pro server
        return HttpResponse("Welcome on the Czechitas webpage")

