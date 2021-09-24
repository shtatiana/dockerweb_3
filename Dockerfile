FROM python:3.8-alpine

WORKDIR /webapp

COPY . /webapp

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "webapp.py"]