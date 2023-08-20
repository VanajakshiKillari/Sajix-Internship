from django.urls import path
from .views import *

urlpatterns = [
    path('student/', studentAPIView.as_view()),
    path('module/', moduleAPIView.as_view())
]