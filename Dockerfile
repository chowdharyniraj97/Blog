FROM python:3.7
#RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc && pip3 install --upgrade pip
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
WORKDIR /projects 
ADD . /projects
RUN pip3 install Flask
RUN pip3 install -r requirements.txt
CMD ["python3","run.py","production"]
