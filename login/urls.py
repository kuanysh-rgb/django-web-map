from django.urls import path

from signup.views import signupaction
from . import views
import signup
from .views import signinaction

urlpatterns = [
    path('', signinaction, name='login'),
    path('home/', views.index, name='home'),
    path('sign-up/', signupaction, name='register'),
    path('sign-in/', signinaction, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login-as-guest', views.login_as_guest, name='login_as_guest')

]