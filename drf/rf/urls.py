from django.urls import path
from .views import *
urlpatterns = [
    path('register/', createsAPI.as_view()),
    path('retrieve/', Get.as_view()),
    path('upd/<int:pk>/', Update.as_view()),
    path('del/<int:pk>/', Destroy.as_view()),
    path('login/', loginView.as_view())
]