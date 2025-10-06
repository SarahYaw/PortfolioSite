FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# Make port 8080 available to the world outside this container
ENV PORT=8080
EXPOSE 8080

# Run app.py when the container launches
CMD ["gunicorn", "-b", ":8080", "wsgi:app"]