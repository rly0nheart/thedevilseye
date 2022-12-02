FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl

RUN python setup.py sdist bdist_wheel
RUN pip install dist/*.whl

ENTRYPOINT ["thedevilseye"]
