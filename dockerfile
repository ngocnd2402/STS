FROM python:3.9-slim

# Copy requirements.txt
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /requirements.txt
RUN sudo apt-get install python-pyaudio


# Set working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Command to run the application
CMD ["python", "main.py"]
