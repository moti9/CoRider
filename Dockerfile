FROM python:3.11.1-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD [ "python", "app.py", "--port", "8080" ]

# CMD [ "python", "app.py" ]