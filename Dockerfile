from python:3.11
label maintainer = 'Fillsogood'

# 도커에서 출력의 결과값 터미널에서 보여줌
env PYTHONUNBUFFERED 1 

copy ./requirements.txt /tmp/requirements.txt
copy ./requirements.dev.txt /tmp/requirements.dev.txt
copy ./app /app

workdir /app
expose 8000

#개발 ture 일 때 사용가능
arg DEV=false 
# 도커가 실행 할 때마다 실행되는 명령어
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true"] ; \
        then echo "===THIS IS DEVELOPMENT BUILD===" && \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

env PATH="/py/bin:${PATH}"

user django-user

