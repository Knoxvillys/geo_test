from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework_gis.filters import DistanceToPointFilter # Фильтр расстояния до точки


from .models import Polygon, LineString, Point
from .serializers import PolygonSerializer, LineStringSerializer, PointSerializer
from .Mixin import CreateListModelMixin



class PolygonView(viewsets.ModelViewSet):
    """

    """
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    

    filter_backends = [DistanceToPointFilter, DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    distance_filter_field = 'geometry'
    distance_filter_convert_meters = True #Для того чтобы преобразовать входное расстояние из метров в градусы


class LineStringView(ListCreateAPIView):
    """

    """
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class PointView(CreateListModelMixin, viewsets.ModelViewSet):
    """

    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
