FROM python:3.6

WORKDIR /usr/src/app

COPY . ./
RUN pip install pipenv
RUN pipenv install

COPY . .

CMD pipenv run python scraper.py