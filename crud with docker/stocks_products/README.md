## Загрузка образа Python версии 3.9
docker pull python:3.9

## Создание сборки образа
docker build -t bcknd_api .

## Запуск контейнера
docker run -d -p 8888:8000 bcknd_api