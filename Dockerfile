FROM python:3.9.8
RUN apt update && apt upgrade -y
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /Telegraph
WORKDIR /Telegraph
COPY bot.py /Telegraph/bot.py
COPY config.py /Telegraph/config.py
RUN python3 bot.py

