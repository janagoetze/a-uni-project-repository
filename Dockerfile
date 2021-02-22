# Dockerfile for running commandline python code
# build it using
# docker build -t a-uni-project --rm .
# run for different commands using
# docker run -it -v `pwd`:/usr/src/app -w /usr/src/app a-uni-project python demo.py
# and
# docker run -it -v `pwd`:/usr/src/app -w /usr/src/app a-uni-project python main.py
# where python demo.py can be replaced by whatever your code documents

# set base image (host OS)
FROM python:3.8-slim

# install requirements here if needed
RUN pip install spacy
RUN python -m spacy download en_core_web_sm

# copy the content of the local src directory to the working directory
COPY . .
