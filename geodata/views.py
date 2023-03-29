from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView

from .models import Polygon, LineString, Point
from .serializers import PolygonSerializer, LineStringSerializer, PointSerializer


class PolygonView(ListCreateAPIView):
    '''
    Создание и получение данных из таблицы "Polygon"
    '''
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer


class LineStringView(ListCreateAPIView):
    '''
    Создание и получение данных из таблицы "LineString"
    '''
    queryset = LineString.objects.all()
    serializer_class = PolygonSerializer


class PointView(ListCreateAPIView):
    '''
    Создание и получение данных из таблицы "Point"
    '''
    queryset = Point.objects.all()
    serializer_class = PolygonSerializer