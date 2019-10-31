from django.urls import path
from . import views
from .views import cadatrar_new

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', cadatrar_new, name='cadastrar'),
    # path('adicionar', views.index, name='index'),
]
