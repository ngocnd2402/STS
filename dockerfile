FROM python:3.9-slim

# Copy requirements.txt
COPY requirements.txt /requirements.txt

# Install dependencies
RUN apt-get update
RUN apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0  -y
RUN pip install --no-cache-dir -r /requirements.txt


# Set working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Command to run the application
CMD ["python", "main.py"]
