from rest_framework import serializers

from .models import Polygon, LineString, Point


class PolygonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Polygon
        fields = '__all__'


class LineStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineString
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'