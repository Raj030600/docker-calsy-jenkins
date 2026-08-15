FROM python:3.12
WORKDIR /try_image
COPY . .
ENTRYPOINT ["python", "docker_calsy.py"]