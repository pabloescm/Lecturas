from rest_framework.routers import DefaultRouter
from lectura.api.lectura_view import LecturaViewSet

router = DefaultRouter()

router.register(r'lecturas', LecturaViewSet)

urlpatterns = router.urls

