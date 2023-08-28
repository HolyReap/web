FROM python:3.9

WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

