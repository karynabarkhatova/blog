from django.urls import path
from .views import current_datatime_now

urlpatterns = [
    path('time/', current_datatime_now),
]