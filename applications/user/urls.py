from django.urls import path

from . import views

app_name = "user_app"

urlpatterns = [
    path(
        'api/google-login/',
        views.LoginSocialAPIView.as_view(), 
    ),
    path(
        'api/register/',
        views.LoginApi.as_view(), 
    ),
    path(
        'api/login/',
        views.ObtainAuthToken.as_view(), 
    ),
]
