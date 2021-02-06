from django.urls import path
from .views import user_log,user_logout

urlpatterns = [
    path("",user_log,name="login"),
    path("logout/",user_logout,name="logout")
]
