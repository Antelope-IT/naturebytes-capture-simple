FROM balenalib/raspberry-pi-python:3.5.7-stretch-run

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /images

COPY . .

CMD ["python", "./capture-simple.py"]