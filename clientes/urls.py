from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name ='index'),
    path('form_cliente/', views.form_cliente, name='form_cliente' ),
    path('detalhe_cliente/<int:id>', views.detalhe_cliente, name = 'detalhe_cliente'),
    path('delete_cliente/<int:id>', views.delete_cliente, name='delete_cliente'),
    path('update_cliente/<int:id>', views.update_cliente, name='update_cliente')
]
