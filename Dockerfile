FROM python:3
WORKDIR /requestcontainer
ADD ./requirements.txt /requestcontainer/requirements.txt
RUN pip install -r requirements.txt
ADD . /requestcontainer
