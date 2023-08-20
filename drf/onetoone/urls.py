from django.urls import path
from .views import *

urlpatterns = [
     path('Library/', Library1View.as_view()),
     path('Book/', Book1View.as_view()),
     path('get/', Get1View.as_view()),
]