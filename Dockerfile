FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings.production
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
RUN mkdir /code
WORKDIR /code
ARG requirements=requirements/production.txt
COPY requirements /code/requirements
RUN pip install -r $requirements
ADD . /code/
