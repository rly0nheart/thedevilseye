FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install build
RUN python -m build
RUN pip install dist/*.whl

ENTRYPOINT ["thedevilseye"]
