# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Set the working directory in the container
WORKDIR /app
# install app
COPY . /app

# final configuration
ENV FLASK_APP=app
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]