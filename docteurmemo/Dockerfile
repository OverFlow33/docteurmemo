###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.18-slim-bookworm as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update
RUN apt-get install -y build-essential python3-dev libldap2-dev libsasl2-dev slapd ldap-utils tox lcov valgrind netcat-traditional

# lint
RUN pip install --upgrade pip

# install python dependencies
COPY ./docteurmemo-db-0.1.tar.gz .
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.18-slim-bookworm

# create directory for the app user
RUN mkdir -p /home/app
# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/core
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update 
RUN apt-get install -y build-essential python3-dev libldap2-dev libsasl2-dev slapd ldap-utils tox lcov valgrind netcat-traditional
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/docteurmemo-db-0.1.tar.gz .
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/core/entrypoint.sh"]