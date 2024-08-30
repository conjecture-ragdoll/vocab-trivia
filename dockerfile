FROM python:3.11-slim

# Install make and other necessary packages
RUN apt-get update && apt-get install -y \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Set the working directory in the container
WORKDIR /app

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment and upgrade pip
RUN /opt/venv/bin/pip install --upgrade pip

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies in the virtual environment
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Make sure commands from venv are callable by default
ENV PATH="/opt/venv/bin:$PATH"

# Command to run your application using make
CMD ["make", "run"]

