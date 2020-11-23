from django.urls import path
from usersApp import views
from .views import UserRegisterView


urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('register', views.register, name="register"),
    path('login/', views.login,name="login"),
    path('logout', views.logout,name="logout"),

    


]