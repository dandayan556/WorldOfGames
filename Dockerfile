FROM python:3.11.2

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY Scores.txt /Scores.txt

CMD ["python", "Live.py"]



