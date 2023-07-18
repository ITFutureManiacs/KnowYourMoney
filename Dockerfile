FROM python:3.10-bullseye

WORKDIR /KnowYourMoney

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN [ "python", "./manage.py", "migrate"]
RUN [ "python", "./manage.py", "loaddata", "users"]
RUN [ "python", "./manage.py", "loaddata", "currencies" ]
RUN [ "python", "./manage.py", "loaddata", "categories" ]
RUN [ "python", "./manage.py", "loaddata", "sources" ]
RUN [ "python", "./manage.py", "loaddata", "expenses" ]
RUN [ "python", "./manage.py", "loaddata", "incomes" ]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
