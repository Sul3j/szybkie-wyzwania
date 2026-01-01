#!/bin/bash
# Quick deploy script for VPS

set -e

echo "🚀 Deploying Szybkie Wyzwania..."

# Variables
VPS_HOST="${VPS_HOST:-your-vps-ip}"
VPS_USER="${VPS_USER:-root}"
APP_DIR="/opt/szybkie-wyzwania"

# SSH and deploy
ssh ${VPS_USER}@${VPS_HOST} << 'ENDSSH'
    set -e

    cd /opt/szybkie-wyzwania

    echo "📥 Pulling new images..."
    docker compose -f docker-compose.prod.yml pull

    echo "🛑 Stopping old containers..."
    docker compose -f docker-compose.prod.yml down

    echo "🚀 Starting new containers..."
    docker compose -f docker-compose.prod.yml up -d

    echo "⏳ Waiting for services to be ready..."
    sleep 10

    echo "📊 Container status:"
    docker compose -f docker-compose.prod.yml ps

    echo "🧹 Cleaning up old images..."
    docker image prune -af

    echo "✅ Deployment completed!"
ENDSSH

echo "🎉 Done! Check https://szybkie-wyzwania.pl"
