FROM python:alpine3.7

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY helloworld helloworld

CMD ["python", "helloworld/manage.py"]