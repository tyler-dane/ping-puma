from django.urls import path

from . import views


urlpatterns = [
    # /pings/
    path('', views.index, name='index'),

    # /pings/add-ping
    path('add-ping/', views.add_ping, name='add-ping'),

    # /pings/add-ping-from-template
    path('add-ping-from-template/', views.add_ping_from_template, name='add-ping-from-template'),

    # /pings/templates/
    path('templates/', views.templates, name='templates'),

    # /pings/1/history/
    path('<int:guest_id>/history/', views.history, name='history')


]
