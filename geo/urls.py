
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from geodata.views import PolygonView, LineStringView, PointView


router = DefaultRouter()
router.register(r'polygon', PolygonView)
router.register(r'linestring', LineStringView)
router.register(r'point', PointView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
