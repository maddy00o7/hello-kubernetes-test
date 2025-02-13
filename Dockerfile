# Use a lightweight Python image
FROM python:3.9-slim
 
# Set the working directory
WORKDIR /app
 
# Copy only the necessary files first
COPY requirements.txt .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the FastAPI application files
COPY . .
 
# Expose the application port
EXPOSE 8000
 
# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
