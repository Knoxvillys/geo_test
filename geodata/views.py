from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status
from rest_framework_gis.filters import DistanceToPointFilter # Фильтр расстояния до точки
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response


from .models import Polygon, LineString, Point
from .serializers import PolygonSerializer, LineStringSerializer, PointSerializer, GpxSerializer
from .Mixin import CreateListModelMixin
from .pars.gpx import LineStringGpx, PoligonGpx, PointGpx



class PolygonView(viewsets.ModelViewSet):
    """

    """
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    

    filter_backends = [DistanceToPointFilter, DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    distance_filter_field = 'geometry'
    # Для того чтобы преобразовать входное расстояние из метров в градусы
    distance_filter_convert_meters = True


class LineStringView(viewsets.ModelViewSet):
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


class FileViewSet(CreateModelMixin, viewsets.ViewSet):
    serializer_class = GpxSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        name = serializer.data.get('name')
        geom_type = serializer.data.get('geom_type')
        file = request.FILES.get('file_upload')
        # проверим что за тип введен
        if geom_type == 'LineString':
            serializer = LineStringSerializer(
                data=LineStringGpx(file).abc_method_geometry()
            )

        elif geom_type == 'Polygon':
            serializer = PolygonSerializer(
                data=PoligonGpx(file).abc_method_geometry()
            )

        elif geom_type == 'MultiPoint':
            serializer = PointSerializer(
                data=PointGpx(file, name=name).abc_method_geometry(),
                many=True
            )

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)