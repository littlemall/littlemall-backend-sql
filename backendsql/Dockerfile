FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/db
WORKDIR /code
ADD requirements.txt /code/
ADD start.sh /code/
RUN pip3 install -r requirements.txt 
RUN pip3 install gunicorn
CMD [ "sh", "./start.sh"]
ADD . /code/