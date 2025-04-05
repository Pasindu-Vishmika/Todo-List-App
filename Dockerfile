# Use the official Python image from the Docker Hub
FROM python:3.12-slim


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
#prevents Python from writing .pyc files to disk.

ENV PYTHONUNBUFFERED=1
#ensures that Python output is sent straight to the terminal without being buffered, making logs available in real-time.

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . /app/

# Run Django commands to make migrations and migrate the 'API' app
RUN python manage.py makemigrations API
RUN python manage.py migrate API


# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
