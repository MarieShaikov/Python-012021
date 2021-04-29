from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from . import models

class KurzyView(ListView):
    model = models.Kurzy
    template_name = "kurzy/kurzy_list.html"

class DetailKurzView(DetailView):
    model = models.Kurzy
    template_name = "kurzy/detail_kurzu.html"

from django.urls import path

from . import views

urlpatterns = [
    path('', views.KurzyView.as_view(), name='index'),
    path('<int:pk>', views.DetailKurzView.as_view(), name='detail_kurzu'),
]