#!/bin/bash

set -e

echo "========================================="
echo "Starting Szybkie Wyzwania deployment..."
echo "========================================="

# Navigate to project directory
cd /opt/szybkie-wyzwania || exit 1

# Pull latest changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull origin main

# Pull latest Docker image from GHCR
echo "Pulling latest Docker image..."
docker compose -f docker-compose.prod.yml pull

# Restart containers with new image
echo "Restarting containers..."
docker compose -f docker-compose.prod.yml up -d --force-recreate

# Wait for containers to start
echo "Waiting for containers to start..."
sleep 10

# Clean up unused Docker resources
echo "Cleaning up Docker resources..."
docker system prune -f

echo "========================================="
echo "Deployment completed successfully!"
echo "========================================="

# Show running containers
docker compose -f docker-compose.prod.yml ps
