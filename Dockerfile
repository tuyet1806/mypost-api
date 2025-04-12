# base on image Python
FROM python:3.10-slim

#install essential libraries
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create an app folder
WORKDIR /app

# Copy requirements abd setting
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy all resources into container
COPY . .

# open 8000 gate
EXPOSE 8000

# run server start function
CMD ["python", "manage.py", "runserver", "*"]