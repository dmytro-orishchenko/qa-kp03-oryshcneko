FROM python:3.8

WORKDIR /usr/src/app/lab2

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]