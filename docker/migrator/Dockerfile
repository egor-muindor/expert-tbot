FROM python:3.9
WORKDIR /var/app
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt
COPY /src .
CMD [ "orator", "migrate", "--config", "orator.yaml", "-f"]
