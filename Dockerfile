# Use Python 3.11 slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for Playwright browsers
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libxss1 \
    libasound2 \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and browser binaries
RUN playwright install --with-deps

# Install Allure CLI globally
RUN npm install -g allure-commandline

# Copy the rest of the application code
COPY . .

# Create reports directory
RUN mkdir -p reports/allure-results reports/allure-report

# Set PYTHONPATH
ENV PYTHONPATH=.

# Default command to run tests
CMD ["pytest", "--alluredir=reports/allure-results"]