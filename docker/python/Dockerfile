FROM python:3.8-slim as base
SHELL ["/bin/bash", "-c"]
WORKDIR /home/url-shortener-user/app

RUN useradd -d /home/url-shortener-user url-shortener-user
RUN chown -R url-shortener-user:url-shortener-user /home/url-shortener-user
ENV PATH "$PATH:/home/url-shortener-user/.local/bin"
ENV FLASK_APP=manage

USER url-shortener-user
COPY ./app/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 3031

FROM base as debug
RUN pip install debugpy
ENV FLASK_ENV=development
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "debugpy", "--listen", "10.10.0.10:5678", "-m", "manage", "--wait-for-client", "--multiprocess", \ 
"-m", "flask", "run", "-h", "10.10.0.10", "-p", "3031" \
]

FROM base as prod
ENV FLASK_ENV=prod
RUN pip install "gunicorn==20.1.0"
CMD ["gunicorn", "--reload", "--bind", "10.10.0.10:3031", "manage:manage"]