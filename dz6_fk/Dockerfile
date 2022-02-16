FROM ubuntu:latest
RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD ./dz4_1.py /src/dz4_1.py
CMD ["python", "/src/dz4_1.py"]
