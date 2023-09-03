from django.urls import path

from . import views
from .views import DrillView

app_name = 'scoring'
urlpatterns = [
    path('', views.DrillView.as_view(), name='drills')
]