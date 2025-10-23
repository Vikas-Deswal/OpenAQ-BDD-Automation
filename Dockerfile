FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    default-jre-headless \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o allure-2.24.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz && \
    tar -zxvf allure-2.24.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure && \
    rm allure-2.24.0.tgz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs allure-results

ENV OPENAQ_API_KEY=""
ENV OPENAQ_BASE_URL="https://api.openaq.org/v3"

CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results"]