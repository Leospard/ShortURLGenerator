FROM python:3.6.3-slim

WORKDIR /home/code
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt 
COPY . .
EXPOSE 9000
CMD ["python3" , "index.py"]