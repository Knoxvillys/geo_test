
from rest_framework import routers

from geodata.views import PolygonView, LineStringView, PointView, FileViewSet


router = routers.SimpleRouter()

router.register('linestring', LineStringView, basename='linestring')
router.register('point', PointView, basename='point')
router.register('polygon', PolygonView, basename='polygon')
router.register('upload', FileViewSet, basename='upload')

urlpatterns = router.urls