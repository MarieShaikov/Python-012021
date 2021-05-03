from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1>Vítejte v naší autopůjčovně!</h1>"
                            "<a href='http://localhost:8000/katalog/seznam/'"
                            ">Seznam aktualne nabizenych aut"
                            "</a><br><h2>Historie naší autopůjčovni</h2> "
                            "<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>"
                            "</a><br><h2>Kontakt</h2> "
                            "<p>tel cislo: +420 000 000 000, email: g.@gmail.com.</p>")

class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam aut.")
