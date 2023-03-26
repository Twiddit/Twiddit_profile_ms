FROM python:3.10

ENV PYTHONNUNBUFFERED 1

RUN mkdir /Twiddit_profile_ms

WORKDIR /Twiddit_profile_ms

COPY . .

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

ARG URL=0.0.0.0:7777

CMD [ "sh", "-c", "python manage.py runserver $URL" ]
