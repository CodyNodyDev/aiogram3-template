FROM python:3.10.12

# Install necessary build dependencies, including libyaml-dev
RUN apt-get update && apt-get install -y libyaml-dev

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install PyYAML separately to avoid build issues
RUN pip install --no-cache-dir PyYAML

# Upgrade pip
RUN pip install --upgrade pip

# Install dbus-python and other dependencies (except PyYAML) first
RUN pip install --no-cache-dir -r requirements.txt --exclude="PyYAML"

# Install the rest of the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Specify the command to run on container start
CMD ["python", "src/main.py"]
