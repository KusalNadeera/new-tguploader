FROM python:3.9.8
RUN apt update && apt upgrade -y
COPY requirements.txt /requirements.txt
COPY bot.py /bot.py
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /Telegraph
WORKDIR /Telegraph
RUN python3 bot.py

