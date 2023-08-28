## Загрузка образа nginx последней версии
docker pull nginx

## Создание образа
docker build -t mynginx .

## Запуск контейнера
docker run -d -p 8888:80 mynginx