FROM python:3.12
WORKDIR /try_image
RUN pip install --no-cache-dir flask
COPY . .
EXPOSE 8080
ENTRYPOINT ["python", "calculator_api.py"]