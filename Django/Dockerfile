FROM python:3.7
WORKDIR /app
COPY . ./
RUN pip install django==2.0.2 django-hosts
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
