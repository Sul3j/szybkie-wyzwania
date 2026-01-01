#!/bin/bash
# Quick log viewing script

VPS_HOST="${VPS_HOST:-your-vps-ip}"
VPS_USER="${VPS_USER:-root}"

echo "📋 Viewing logs from VPS..."
echo "Press Ctrl+C to exit"
echo ""

ssh ${VPS_USER}@${VPS_HOST} "cd /opt/szybkie-wyzwania && docker compose -f docker-compose.prod.yml logs -f --tail=100"
