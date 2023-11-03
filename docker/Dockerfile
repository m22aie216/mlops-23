#FROM ubuntu:23.10
FROM python:3.9.17
COPY . /digits/
#RUN apt-get update
#RUN apt-get install -y python3
#RUN apt-get install -y python3-pip
RUN pip install --no-cache-dir -r /digits/requirements.txt
RUN mkdir /digits/models
WORKDIR /digits
CMD ["python","./digits/exp.py --runs 4 --test_sizes 0.2,0.3 --dev_sizes 0.2 --models svm,tree"]
