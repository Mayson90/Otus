# BUILD THIS APP:
# start build:
# $ docker build . -t flask_app
# start container:
# $ docker run -p 4321:5000 flask_app
# got yo your localhost http://http://127.0.0.1:4321/

FROM python

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]