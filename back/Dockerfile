FROM python

EXPOSE 5000
CMD ["python", "app.py"]
ENV ARCHFLAGS -Wno-error=unused-command-line-argument-hard-error-in-future
RUN mkdir /code
RUN mkdir /required
WORKDIR /required
COPY requirements.txt /required/requirements.txt
RUN pip install -r /required/requirements.txt
WORKDIR /code
ADD ./py_app /code



