from django.urls import path
from localizador.views import homepage

urlpatterns = [
    path('', homepage),
]
