#Dockerfile za Server

FROM python:3.8

WORKDIR /ServerBase

COPY ./app.py /ServerBase/

EXPOSE 8081

RUN pip install flask

CMD ["python","app.py"]