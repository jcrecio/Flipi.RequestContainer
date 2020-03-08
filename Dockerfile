FROM python:3
ADD . /f
WORKDIR /f
RUN pip install -r requirements.txt