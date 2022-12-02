FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl

RUN pip install --upgrade pip && pip install build && python -m build
RUN pip install dist/*.whl

ENTRYPOINT ["thedevilseye"]
