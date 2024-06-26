FROM python:3.9-slim

# Copy requirements.txt
COPY requirements.txt /requirements.txt

# Install dependencies
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN apt-get install gcc -y
RUN pip install --no-cache-dir -r /requirements.txt

# Set working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Command to run the application
CMD ["python", "main.py"]