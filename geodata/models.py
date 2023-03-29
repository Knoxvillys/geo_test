from django.contrib.gis.db import models


class LineString(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя.')
    geometry = models.LineStringField(verbose_name='Поле геометрии. ')

    def __str__(self):
        return self.name


class Point(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    geometry = models.PointField(verbose_name='Поле геометрии. ')


    def __str__(self):
        return self.name


class Polygon(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    geometry = models.PolygonField(verbose_name='Поле геометрии. ')
    points = models.ManyToManyField(Point, blank=True, verbose_name='Точки.')

    def __str__(self):
        return self.name