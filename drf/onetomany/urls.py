from django.urls import path
from .views import *

urlpatterns = [
     path('Library/', LibraryView.as_view()),
     path('Book/', BookView.as_view()),
     path('get/', GetView.as_view()),
]