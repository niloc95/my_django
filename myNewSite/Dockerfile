FROM python:3.10.6
WORKDIR /myNewsite/mydsite
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python","manage.py","runserver", "localhost:9000"]