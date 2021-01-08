from rest_framework import routers
from .api import HeroViewSet

router = routers.DefaultRouter()
router.register('api/myapi', HeroViewSet, 'heros')

urlpatterns = router.urls