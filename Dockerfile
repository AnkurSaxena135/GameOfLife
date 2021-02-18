FROM python:3.8-buster as builder

RUN pip install virtualenv
RUN virtualenv -p python3.8 /env

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate. This ensures the application is executed within
# the context of the virtualenv and will have access to its dependencies.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN mkdir -p /usr/src
WORKDIR /usr/src

ADD . /usr/src
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "game_of_life/game_of_life.py"]
CMD ["20"]