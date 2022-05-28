#Dockerfile za Client-a

FROM python:3.8

WORKDIR /ClientBase

COPY ./request.py /ClientBase/

EXPOSE 8081

RUN pip install requests

CMD ["python","request.py"]