# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY src /app

# Include the "static" directory

# Install your Python dependencies and create the virtual environment
COPY requirements.txt /app/requirements.txt
RUN /app/myenv/bin/pip install -r /app/requirements.txt

# Expose the port on which the FastAPI app will run
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
