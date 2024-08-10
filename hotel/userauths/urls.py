
from django.urls import path
from  . views import Registrationview
urlpatterns = [
    path("signup",Registrationview,name="signup")
]
