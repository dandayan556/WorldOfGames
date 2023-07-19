FROM python:3.11.2

WORKDIR /MyDockFile

RUN python --version

COPY requierments.txt .

RUN pip install --upgrade pip && pip install -r requierments.txt

COPY Scores.txt /MyDockFile/Scores.txt

COPY . .

CMD ["python", "-u", "mainScores.py"]



