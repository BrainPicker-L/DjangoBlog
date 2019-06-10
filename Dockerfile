FROM python:3.6-alpine3.8
MAINTAINER lzz122zzl@163.com
ENV pythonunbuffered 1
WORKDIR /opt
COPY requirements.txt /opt/requirements.txt
RUN apk add --no-cache --update python3-dev  gcc build-base
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache openssl-dev
RUN apk add --no-cache gcc musl-dev libxslt-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install -r requirements.txt
RUN apk add --no-cache bash
EXPOSE 8000
COPY . /opt
