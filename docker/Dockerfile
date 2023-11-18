#FROM ubuntu:23.10
FROM python:3.9.17
COPY . /digits/
#RUN apt-get update
#RUN apt-get install -y python3
#RUN apt-get install -y python3-pip
WORKDIR /digits
RUN pip install --no-cache-dir -r /digits/requirements.txt
VOLUME ["/digits"]
ENV FLASK_APP api/app.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
#docker run -it -p 5000:5000 digits/v1 bash
#CMD ["mkdir", "/digits/models"]
#CMD ["python3","/digits/exp.py --runs 4 --test_sizes 0.3 --dev_sizes 0.2 --models svm,tree"]
