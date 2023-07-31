from django.urls import path
from .views import search_meaning

app_name = 'dict'

urlpatterns = [
    path('', search_meaning, name='search'),
]