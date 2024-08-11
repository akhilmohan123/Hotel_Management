
from django.urls import path
from  . views import Registrationview,Logoutview
urlpatterns = [
    path("signup",Registrationview,name="signup"),
    path("logout",Logoutview,name="logout")

]
