FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# system depends
RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip

# no need for the explicit target path because we've already set WORKDIR as /usr/src/app above
COPY ./requirements.txt .
RUN pip install -r requirements.txt

########## TODO: pretty sure we could some cache-prevention or cleanup ###########

# again WORKDIR is already /usr/src/app
RUN echo $(ls)
COPY . .

# entrypoint
ENTRYPOINT ["./entrypoint.sh"]