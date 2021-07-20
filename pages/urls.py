from pages.views import home
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
]
