# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Include the "static" directory

RUN pip install -r requirements.txt

# Expose the port on which the FastAPI app will run
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
