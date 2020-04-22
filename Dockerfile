FROM python:3.8-alpine

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH \
    && chmod -R 777 $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]