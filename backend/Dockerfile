FROM python:3.6

WORKDIR '/app/backend'

COPY requirements.txt .
RUN pip install --upgrade pip -r requirements.txt
COPY . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000