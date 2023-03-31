from rest_framework import serializers, SlugRelatedField
from rest_framework_gis.serializers import GeoFeatureModelSerializer # сериализатор для GeoJISON

from .models import Polygon, LineString, Point


class PolygonSerializer(GeoFeatureModelSerializer):
    points = SlugRelatedField(
        queryset=Point.objects.all(),
        allow_null=True,
        required=False,
        slug_field='name',
        many=True
    )
    
    class Meta:
        model = Polygon
        geo_field = "geometry" # требуется для определения GeoFeatureModelSerializer
        id_field = False # Первичный ключ модели (обычно атрибут «id») автоматически используется в качестве id поля каждого объекта GeoJSON Feature Object .
        fields = ['geometry', 'id', 'name', 'points']


class LineStringSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = LineString
        geo_field = "geometry"
        id_field = False
        fields = ['geometry', 'id', 'name']


class PointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Point
        geo_field = 'geometry'
        id_field = False
        fields = ['geometry', 'id', 'name']


class GpxSerializer(Serializer):
    name = CharField(allow_blank=True)
    geom_type = CharField() # я бы выбрал ChoiceField, но задание просит другое
    file = FileField()

    def validate(self, data):
        if data['geom_type'] not in ('LineString', 'Polygon',  'MultiPoint'):
            raise ValidationError("Дружок правильно выбери LineString, Polygon или MultiPoint")

        elif str(data['file'])[-4:] != '.gpx':
            raise ValidationError("Ожидается  формат .gpx")

        return data

    class Meta:
        fields = ['name', 'geom_type', 'file']
