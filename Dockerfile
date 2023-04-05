## За базу используем официальный image питона
#FROM python:3.7
#
## Отключаем буферизацию логов
#ENV PYTHONUNBUFFERED 1
#
## Обновляем пакетный менеджер
#RUN apt-get update -y && apt-get upgrade -y
#
## Ставим зависимости GDAL, PROJ
#RUN apt-get install -y gdal-bin libgdal-dev
#RUN apt-get install -y python3-gdal
#RUN apt-get install -y binutils libproj-dev
#
## Изходя из зависимостей добавляем библиотеки в контейнер
#RUN pip install --upgrade pip
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
#
## Копируем все файлы приложения в рабочую директорию в контейнере
#COPY . /srv/html/geo
#WORKDIR /srv/html/geo

FROM python:3.7-slim-buster
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Обновляем пакетный менеджер
RUN apt-get update -y && apt-get upgrade -y

# Ставим зависимости GDAL, PROJ
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN chmod 755 entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["run"]