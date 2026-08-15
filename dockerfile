FROM python:3.12
WORKDIR /try_image
COPY . .
CMD ["python", "docker_calsy.py"]