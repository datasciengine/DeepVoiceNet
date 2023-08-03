FROM python:3.8
LABEL authors="MSAHIN"
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
WORKDIR /code
COPY ./* /code
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
CMD ["python3", "app.py"]