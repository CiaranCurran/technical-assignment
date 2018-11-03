FROM python:3.6-alpine

RUN adduser -D wordcountapp

WORKDIR /home/wordcountapp

COPY requirements.txt requirements.txt
COPY nltk_data nltk_data
RUN apk update
RUN apk add gcc
#RUN apk add curl
RUN apk add libxml2-dev libxslt-dev libc-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn
#RUN pip install -U textblob
#RUN curl https://raw.github.com/sloria/TextBlob/master/download_corpora.py | python
#RUN python -m nltk.downloader -d /home/wordcountapp/nltk_data all-corpora
ENV NLTK_DATA /home/wordcountapp/nltk_data/

COPY app app
COPY wordCount.py config.py ./

ENV FLASK_APP wordCount.py

RUN chown -R wordcountapp:wordcountapp ./
USER wordcountapp

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["wordCount.py"]