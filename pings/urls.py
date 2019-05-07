from django.urls import path

from . import views


urlpatterns = [
    # ex: /pings/
    path('', views.index, name='index'),

    # ex: /pings/1
    #path('<int:guest_id>/', views.templates, name='templates'),

    # ex: /pings/templates/
    path('templates/', views.templates, name='templates'),

    # ex: /pings/1/custom/
    path('<int:guest_id>/custom/', views.custom, name='custom'),

    # ex: /pings/1/history/
    path('<int:guest_id>/history/', views.history, name='history'),

    path('formtest/', views.ping_form_test, name='formtest')
]
