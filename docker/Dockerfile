FROM python:3.9.17
COPY . /digits/
WORKDIR /digits
RUN pip install --no-cache-dir -r /digits/requirements.txt
EXPOSE 443
ENV FLASK_APP api/app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=443"]
