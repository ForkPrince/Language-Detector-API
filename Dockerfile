FROM python:3.11.6-alpine3.18

RUN apk update

RUN mkdir /app

WORKDIR /app

RUN pip install flask ShortLanguageDetection

COPY . .

COPY ./lib/dict /usr/local/lib/python3.11/site-packages/ShortLanguageDetection/DictDetector/dict

COPY ./lib/languages.json /usr/local/lib/python3.11/site-packages/ShortLanguageDetection/DictDetector/languages.json

COPY ./lib/models /usr/local/lib/python3.11/site-packages/ShortLanguageDetection/models

EXPOSE 5000

CMD ["python", "./app.py"]