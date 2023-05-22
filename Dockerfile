FROM python:3.11-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

#WORKDIR /app/db
CMD ["python", "create_tables.py"]
#CMD sleep 1500
