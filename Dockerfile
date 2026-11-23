FROM python:3.15.2-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py config.ini .

# Create persistent storage directory for DNS records (data volumes will bind to this)
RUN mkdir -p /app/data && chown -R $(id -u):$(id -g) /app/data

# Expose port 53 for DNS
EXPOSE 53

# Run the DNS server
CMD ["python", "server.py"]