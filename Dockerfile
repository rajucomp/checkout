# Use a Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the application port
EXPOSE 5000

ENV FLASK_APP=src/app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
