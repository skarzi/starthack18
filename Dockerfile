FROM python:latest
MAINTAINER Wouter Menninga <mail@woutermenninga.nl>

ADD . /var/app
WORKDIR /var/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
