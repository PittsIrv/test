# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire Django app to the container
COPY . .

# Expose the port your Django app will listen on (default is 8000)
EXPOSE 8000

# Define the command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
