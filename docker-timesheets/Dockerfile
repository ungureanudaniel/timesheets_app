# pull official base image
FROM python:3.10.8-slim

# set work directory
WORKDIR /usr/src/docker-timesheets/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/docker-timesheets/entrypoint.sh
RUN chmod +x /usr/src/docker-timesheets/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/docker-timesheets/entrypoint.sh"]