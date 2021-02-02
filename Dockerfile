# Dockerfile for running commandline python code
# build it using
# docker build -t a-uni-project --rm .
# run it using
# docker run -it --name homework_solution --rm a-uni-project
# then the code can be called, e.g. python demo.py

# set base image (host OS)
FROM python:3.8-slim

# an arbitrary app user
RUN useradd --create-home --shell /bin/bash app_user

# set the working directory in the container
WORKDIR /home/app_user

# install requirements here if needed

# change user
USER app_user

# copy the content of the local src directory to the working directory
COPY . .

# for commandline usage of code
CMD ["bash"]
