FROM alpine

EXPOSE 5000
CMD ["python", "app.py"]
ENV ARCHFLAGS -Wno-error=unused-command-line-argument-hard-error-in-future
RUN mkdir /code
WORKDIR /code
ADD ./py_app /code

RUN apk add --no-cache python \
    python-dev \
    py-pip  gcc gfortran &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt

