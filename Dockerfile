FROM python:3.11
LABEL maintainer = 'Fillsogood'

# 도커에서 출력의 결과값 터미널에서 보여줌
ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
COPY ./scripts /scripts


WORKDIR /app
EXPOSE 8000

#개발 ture 일 때 사용가능
ARG DEV=false 
# 도커가 실행 할 때마다 실행되는 명령어
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get update && \
    apt-get install -y postgresql-client build-essential libpq-dev zlib1g zlib1g-dev && \
    if [ $DEV = "true" ] ; \
        then echo "===THIS IS DEVELOPMENT BUILD===" && \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    apt-get remove -y --purge build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin/:$PATH"

USER django-user

CMD ["run.sh"]
