FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
# Install dependencies
# RUN pip install uv --trusted-host pypi.org --trusted-host files.pythonhosted.org

RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org  --proxy=http://cloudproxy.auiag.corp:8080

# Copy the application code
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]