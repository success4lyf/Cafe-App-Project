FROM python:latest

WORKDIR /usr/app/src

RUN pip install pymysql

RUN pip install python-dotenv

COPY connect_db.py ./

# CMD ["python", "./mysql_db.py"]