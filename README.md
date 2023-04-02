GeoDjango

Для запуска : 

```
docker-compose up
```

ссылки(Endpoints) на "точки":

```
127.0.0.1:8000/api/upload/
```
Сохранение данных из файла:
```
POST заброс на добавление файла формата gpx
```
```
Имеет поля для заполнения:
  name - текстовое поле
  geom_type - текстовое поле обязательно прописать `LineString`, `Polygon`,  `MultiPoint`
  file - форма для добафления файла формата gpx
```


127.0.0.1:8000/api/linestring/
```
GET: Получение списка из бд
POST: Есть возможность добавить списком. Одним запросом в БД!
есть возможность фильтрации.
```
POST:
```json
{
   "name": "Линия 1",
   "geometry": {
      "type": "LineString",
      "coordinates": [
            [
                92.899501,
                57.34302
            ],
            [
                93.899501,
                58.34302
            ],
            [
                94.899501,
                59.34302
            ]
      ]
   }
}
```
127.0.0.1:8000/api/linestring/<int:pk>
```
GET: Получение по ID
PUT: Изменение по ID
DELETE: Удаление по ID
```
GET:
```json
{
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [
            ...
        ]
    },
    "properties": {
        "id": 1,
        "name": "Линия №2018"
    }
}
```

```
127.0.0.1:8000/api/point/
```
```
GET: Получение списка из бд
POST: Есть возможность добавить списком. Одним запросом в БД!
есть возможность фильтрации.
```
POST JSON один:
```json
{
   "name": "Точка 1",
   "geometry": {
      "type": "Point",
      "coordinates": [
         92.899501,
         58.34302
      ]
   }
}
```
Вариант списком:
```json
[
  {
    "name": "Точка 1",
    "geometry": {
      "type": "Point",
      "coordinates": [
        92.899501,
        58.34302
      ]
    }
  },
  {
    "name": "Точка 2",
    "geometry": {
      "type": "Point",
      "coordinates": [
        93.899501,
        59.34302
      ]
    }
  },
  ...
]
```
GET:
```json
{
"type": "FeatureColection",
"features": [
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                92.899501,
                58.34302
            ]
        },
        "properties": {
            "id": 144,
            "name": "Точка 111"
        }
    },
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                92.899501,
                58.34302
            ]
        },
        "properties": {
            "id": 145,
            "name": "Точка 1111"
        }
    }
]
```
127.0.0.1:8000/api/point/<int:pk>
```
GET: Получение по ID
PUT: Изменение по ID
DELETE: Удаление по ID
```
GET:
```json
{
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [
            58.297538105220404,
            92.80998236626284
        ]
    },
    "properties": {
        "id": 2,
        "name": "point1234"
    }
}
```

127.0.0.1:8000/api/polygon/
```
GET: Получение списка из бд
POST: Есть возможность добавить списком. Одним запросом в БД!
есть возможность фильтрации, пои названию и в пределах заданного радиуса отнносительно точки.
```
GET:
```json
{
   "name": "Полигон 1",
   "geometry": {
      "type": "Polygon",
      "coordinates": [
            ...
      ]
   }
}
```
127.0.0.1:8000/api/polygon/<int:pk>
```
GET: Получение по ID
PUT: Изменение по ID
DELETE: Удаление по ID
```
POST:
```json
{
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            ...
        ]
    },
    "properties": {
        "id": 1,
        "name": "Полигон №2018"
    }
}
```
