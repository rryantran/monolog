# Use Python 3.12 image (slim for reduced image size)
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /

# Copy requirements file into the container
COPY requirements.txt .

# Install required packages (no caching packages to reduce image size)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into the container
COPY . .

# Run bot script
CMD ["python3", "bot.py"]