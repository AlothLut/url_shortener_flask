FROM python:3.8-slim as base
SHELL ["/bin/bash", "-c"]
WORKDIR /home/url-shortener-user/app

RUN useradd -d /home/url-shortener-user url-shortener-user
RUN chown -R url-shortener-user:url-shortener-user /home/url-shortener-user
ENV PATH "$PATH:/home/url-shortener-user/.local/bin"
ENV FLASK_APP=app.py

USER url-shortener-user
COPY ./app/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 3031

FROM base as debug
RUN pip install debugpy
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

FROM base as prod
RUN pip install "gunicorn==20.1.0"
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:3031", "app:app"]