# Use Python 3.11 slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for Playwright browsers
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    procps \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    libnotify-dev \
    libgconf-2-4 \
    libnss3-dev \
    libxss1 \
    libasound2-dev \
    libxtst6 \
    xauth \
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