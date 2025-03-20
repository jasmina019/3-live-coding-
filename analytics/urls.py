from django.urls import path
from . import views


urlpatterns = [
    path('analytics/temperature-avg/', views.average_temperature_view, name='temperature-avg')
]