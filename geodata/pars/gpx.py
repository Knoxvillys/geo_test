"""
По идее это обычный xml но внутри как будь то абстракция 1. tracks 2. segments 3. points
gpx = gpxpy.parse(open('Точки.gpx'))

print("{} track(s)".format(len(gpx.tracks)))
track = gpx.tracks[0]

print("{} segment(s)".format(len(track.segments)))
segment = track.segments[0]

print("{} point(s)".format(len(segment.points)))
результат
1 track(s) <- в них лежат типы как в xml
               |
1 segment(s) <-
              |
15 point(s) <-
"""
import gpxpy.gpx
from abc import ABC, abstractmethod
from dataclasses import dataclass


# декоратор помогает аннотировать типы, но короче, см. в кингу "декораторы"
@dataclass
class Book:
    name: str
    point: str


class ParseGpx:
    """
    парсим gpx, из tracks достаем segments из него points
    кладем в строку и список
    """
    def __init__(self, file):
        self.file = file

    def pars(self):
        name = ''
        points = []
        gpx = gpxpy.parse(self.file)
        
        for tracks_item in gpx.tracks:
            # Это строка, а не список .append тут не подойдет переадресуем (=)
            name = tracks_item.name # там лежит имя (trk - track)
            for segments_item in tracks_item.segments: # там  лежит точка (trkseg - track segment - segment)
                for points_item in segments_item.points:
                    # В одной точке 2 параметра (широта, долгота)
                    # их нужно в список добавить поэтому не присваиваем = points
                    points.append([point.latitude, point.longitude])

        return Book(name=name, point=point,)


class GeoItems(ABC):
    def __init__(self, file):
        self.parser = ParsePpx
        self.file = file

        @abc.abstractmethod
        def abc_method_geometry(self):
            pass


class LineStringGpx(GeoItems):
    def abc_method_geometry(self):
        data = self.parser(self.file).pars()
        line_string_data = {
            'name': data.name,
            'geometry': {
                'type': 'LineString',
                'coordinates': data.points
            }
        }

        return line_string_data


class PoligonGpx(GeoItems):
    def abc_method_geometry(self):
        data = self.parser(self.file).pars()
        polygon_data = {
            'name': data.name,
            'geometry': {
                'type': 'Polygon',
                'coordinates': [data.points, ]
            }
        }

        return polygon_data


class PointGpx(GeoItems):
    def abc_method_geometry(self):
        data = self.parser(self.file).pars()
        point_list = ()
        pint_data = list(point_list)
        for item, point in enumerate(self.point): # enumerate достает число по порядку и точу соответствующую порядку
            pint_data.append({
                'name': data.name + str(item), # Добавляем число из enumerate(item)
                'geometry': {
                    'type': 'Point',
                    'coordinates': point
                }
            })
            return pint_data