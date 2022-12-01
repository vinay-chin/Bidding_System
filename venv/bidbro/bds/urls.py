from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from . import views

urlpatterns=[
  path('', views.index),
  path('logreg', views.logreg),
  path('login', views.login, name="login"),
  path('signup', views.signup, name="signup"),
  path('logout', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
  path('form_feedback', views.form_feedback),
]