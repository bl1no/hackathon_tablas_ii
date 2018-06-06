FROM python

EXPOSE 5000
CMD ["python", "app.py"]
ENV ARCHFLAGS -Wno-error=unused-command-line-argument-hard-error-in-future
RUN mkdir /code
WORKDIR /code
ADD ./py_app /code

RUN pip install -r requirements.txt

