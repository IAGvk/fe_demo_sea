FROM public.docker.nexus3.auiag.corp/library/python:3.12.7-slim AS base

# for vm
ARG http_proxy
ARG https_proxy

COPY ca-bundle.pem /usr/local/share/ca-certificates/ca-bundle.crt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates
# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Set PYTHONPATH
ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    REQUESTS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt" \
    SSL_CERT_FILE="/etc/ssl/certs/ca-certificates.crt" \
    CURL_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt" \
    GRPC_DEFAULT_SSL_ROOTS_FILE_PATH="/etc/ssl/certs/ca-certificates.crt"\
    NODE_EXTRA_CA_CERTS="/etc/ssl/certs/ca-certificates.crt" 
  
# for vm
ENV http_proxy=http://cloudproxy.auiag.corp:8080 \
    https_proxy=http://cloudproxy.auiag.corp:8080

RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org  --proxy=http://cloudproxy.auiag.corp:8080

# Copy the application code
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "frontend_main.py", "--server.port=8501", "--server.address=0.0.0.0"]