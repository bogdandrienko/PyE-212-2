FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_app_dir
WORKDIR /docker_app_dir
COPY requirements.txt /docker_app_dir/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /docker_app_dir/

