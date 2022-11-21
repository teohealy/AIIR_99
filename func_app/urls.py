from django.urls import path
from . import views


urlpatterns = [
    path('<int:a>/<inbt:b>', views.index(), name='index')
]