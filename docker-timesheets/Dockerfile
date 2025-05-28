# pull official base image
FROM python:3.12-slim-bookworm

# set work directory
WORKDIR /usr/src/docker-timesheets

# set environment variables
# Avoid writing `.pyc` files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint script and ensure it's executable
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# copy project
COPY . .

# Entrypoint to wait for DB and run migrations, etc.
ENTRYPOINT ["./entrypoint.sh"]