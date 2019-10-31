from django.urls import path
from . import views
from .views import cadatrar_new
from .views import cadastrar_update

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', cadatrar_new, name='cadastrar'),
    path('update/<int:id>/', cadastrar_update, name='atualizar'),
]

