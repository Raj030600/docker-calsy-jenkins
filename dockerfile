FROM python:3.12
WORKDIR /try image
COPY . .
CMD ["python", "docker_calsy.py"]