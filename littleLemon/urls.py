from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    #path('dishes/<str:name>', views.menuitems, name='menuitems'),
    path('', views.form_view),
]