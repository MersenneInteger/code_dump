FROM python:3
#FROM mongo:3.6.4
WORKDIR /usr/src/app
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt
COPY . .
CMD ["python", "app.py"]
