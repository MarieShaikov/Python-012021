from django.urls import path
from . import views


urlpatterns = [
    path('', views.KurzyView.as_view(), name='index'),
    path('<int:pk>', views.DetailKurzView.as_view(), name='detail_kurzu'),
    path('prihlaska/', views.VytvorPrihlasku.as_view(), name='prihlaska'),
    path('prihlaska/potvrzeni/', views.PotvrzeniPrihlasky.as_view(), name='potvrzeni_prihlasky'),
]

