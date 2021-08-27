from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('c/<int:id>', views.community),
    path('create', views.create),
    path('login', views.loginPage),
    path('post/<int:id>', views.post),
    path('register', views.register),
    path('u/<int:id>', views.user),
    path('settings', views.settings),
    path('logout', views.logoutUser),
    path("create-community", views.createCommunity),
    path("search", views.search)
]
