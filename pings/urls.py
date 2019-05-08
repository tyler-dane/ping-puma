from django.urls import path

from . import views


urlpatterns = [
    # /pings/
    path('', views.index, name='index'),

    # /pings/add_ping
    path('add_ping/', views.add_ping, name='add_ping'),

    # /pings/templates/
    path('templates/', views.templates, name='templates'),

    # /pings/1/history/
    path('<int:guest_id>/history/', views.history, name='history')


]
