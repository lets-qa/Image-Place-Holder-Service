# Use a smaller Python base image (slim variant to reduce size)
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code into the container
COPY . /app

# Expose port 80 (the container's listening port)
EXPOSE 80

# Run uvicorn server on container startup
CMD ["uvicorn", "img_place_holder:app", "--host", "0.0.0.0", "--port", "80"]
