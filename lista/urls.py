from django.urls import path
from . import views
from .views import cadatrar_new
from .views import cadastrar_update
from .views import cadastrar_delete

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', cadatrar_new, name='cadastrar'),
    path('update/<int:id>/', cadastrar_update, name='atualizar'),
    path('delete/<int:id>/', cadastrar_delete, name='deletar'),
]

