FROM python:3
ADD . /requestcontainer
WORKDIR /requestcontainer
RUN pip install -r requirements.txt