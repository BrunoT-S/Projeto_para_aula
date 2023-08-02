from django.urls import path
from . import views 

urlpatterns = [

    path('',views.main,name='main'),
    path('cadastrar', views.cadastro, name='cadastro'),
    path('vizulaizacao',views.visualizar, name='ver'),
    path('Update/<str:pk>',views.Update, name='Update'),
    path('Deletar/<str:pk>',views.Delete, name='Delete'),
    path('signup',views.signup_view, name='Signup'),
    path('login',views.login_view, name='Login'),
    path('logout',views.logout_view, name='Logout'),
    path('painel',views.painel_usuario, name='pgn_usu'),
]
