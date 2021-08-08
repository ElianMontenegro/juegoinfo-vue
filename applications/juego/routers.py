from rest_framework import routers

from .viewsets import JuegoViewSet

router = routers.SimpleRouter()
router.register(r'juego', JuegoViewSet ,basename="juego")

urlpatterns = router.urls