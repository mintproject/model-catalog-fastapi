FROM python:3.8 AS builder

WORKDIR /usr/src/app
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --upgrade pip
COPY . .
RUN pip install --no-cache-dir .
RUN pip install -r requirements.txt
ENV PATH=/venv/bin:$PATH
