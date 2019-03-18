FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements-deploy.txt ./
RUN pip install -r requirements.txt -r requirements-deploy.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000
ENTRYPOINT ["./run_production.sh"]
