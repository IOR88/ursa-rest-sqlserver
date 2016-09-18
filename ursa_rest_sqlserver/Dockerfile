FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python3.5-dev \
    unixodbc-dev \
    freetds-dev \
    tdsodbc \
    python-pip



ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN ln -sf /code/conf/freetds.conf /etc/freetds/freetds.conf
RUN ln -sf /code/conf/odbcinst.ini /etc/odbcinst.ini


