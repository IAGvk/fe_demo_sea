FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org  --proxy=http://cloudproxy.auiag.corp:8080

# Copy the application code
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "frontend_main.py", "--server.port=8501", "--server.address=0.0.0.0"]