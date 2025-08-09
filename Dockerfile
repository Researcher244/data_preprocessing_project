# Use an official Python runtime as a parent image.
# This will include a specific version of Python and a base operating system.
FROM python:3.11-slim

# Set the working directory in the container to /app
# This is where all of your project files will live inside the container.
WORKDIR /app

# Copy the requirements.txt file into the container.
# This is a very common best practice to ensure dependencies are installed first.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt.
# The `--no-cache-dir` flag prevents caching, saving space in the image.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container.
# This copies your preprocess_data.py and any other files you have.
COPY . .

# Define the command to run the Python script when the container starts.
# This is the last thing that happens when the container is run.
CMD ["python", "preprocess_data.py"]