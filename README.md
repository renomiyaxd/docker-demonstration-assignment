Steps to do it.

1. Tasks

Version 1: Display Sample Text
Version 2: Display OS Information
Version 3: Log Access to PostgreSQL

2. Package the Application and Data Storage as Docker Images
Build Docker Images for Each Version

# Build Version 1
docker build -t web-app:v1 -f Dockerfile .
# Build Version 2
docker build -t web-app:v2 -f Dockerfile .
# Build Version 3
docker build -t web-app:v3 -f Dockerfile .

3. Ensure Image Security Best Practices
> Use a minimal base image/ lightweight image like python:3.9-slim to reduce vulnerabilities.
> Use --no-cache-dir in pip install to prevent unnecessary files.
> Set specific Python package versions in requirements.txt.

4. Demo the Web Application Running in a Container

# Run Version 1
docker run -d -p 5001:5000 --name web-app-v1 web-app:v1
# Run Version 2
docker run -d -p 5002:5000 --name web-app-v2 web-app:v2
# Set up PostgreSQL for Version 3
docker network create web-app-network

docker run -d --name db \
  --network web-app-network \
  -e POSTGRES_DB=yourdb \
  -e POSTGRES_USER=youruser \
  -e POSTGRES_PASSWORD=yourpassword \
  postgres:15

# Initialize the PostgreSQL database
docker exec -it db psql -U youruser -d yourdb -c \
  "CREATE TABLE access_logs (id SERIAL PRIMARY KEY, timestamp TIMESTAMP, ip VARCHAR(50));"

# Run Version 3
docker run -d -p 5003:5000 --name web-app-v3 \
  --network web-app-network \
  web-app:v3

# Apply Kubernetes Manifests
kubectl apply -f deployment.yaml
kubectl port-forward svc/web-app-service 8080:80

# To exec into the DB (via Docker)
docker exec -it db /bin/bash
psql -U youruser -d yourdb

# End of document