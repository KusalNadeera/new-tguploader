FROM python:3.9.8
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /Telegraph
WORKDIR /Telegraph
RUN python3 bot.py

