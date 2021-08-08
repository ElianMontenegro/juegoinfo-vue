from django.urls import path

from . import views

app_name = "juego_app"

urlpatterns = [
    path(
        'api/list-juegos', 
        views.JuegosListApiView.as_view(),
    ),
    path(
        'api/create-juegos', 
        views.JuegosCreateApiView.as_view(),
    ),
    path(
        'api/juego/<pk>', 
        views.JuegosUpdateDetailApiView.as_view(),
    ),
    path(
        'api/juego/delete/<pk>', 
        views.JuegosDeleteApiView.as_view(),
    ),
    path(
        'api/juego/search/', 
        views.JuegosListApiView.as_view(),
    ),
]