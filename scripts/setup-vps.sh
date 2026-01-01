#!/bin/bash
# Initial VPS setup script - run once on VPS

set -e

echo "🔧 Setting up VPS for Szybkie Wyzwania..."

# Update system
echo "📦 Updating system..."
sudo apt update && sudo apt upgrade -y

# Install Docker
echo "🐳 Installing Docker..."
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
else
    echo "✅ Docker already installed"
fi

# Install Docker Compose
echo "📦 Installing Docker Compose..."
if ! docker compose version &> /dev/null; then
    sudo apt install docker-compose-plugin -y
else
    echo "✅ Docker Compose already installed"
fi

# Install Nginx
echo "🌐 Installing Nginx..."
if ! command -v nginx &> /dev/null; then
    sudo apt install nginx -y
    sudo systemctl enable nginx
    sudo systemctl start nginx
else
    echo "✅ Nginx already installed"
fi

# Install Certbot
echo "🔒 Installing Certbot..."
if ! command -v certbot &> /dev/null; then
    sudo apt install certbot python3-certbot-nginx -y
else
    echo "✅ Certbot already installed"
fi

# Create app directory
echo "📁 Creating application directory..."
sudo mkdir -p /opt/szybkie-wyzwania
sudo chown $USER:$USER /opt/szybkie-wyzwania

cd /opt/szybkie-wyzwania
mkdir -p {logs,static,media,postgres_data,redis_data,backups}

# Setup firewall
echo "🔥 Configuring firewall..."
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
echo "y" | sudo ufw enable || true

echo "✅ VPS setup completed!"
echo ""
echo "Next steps:"
echo "1. Copy docker-compose.prod.yml to /opt/szybkie-wyzwania/"
echo "2. Create .env file with your secrets"
echo "3. Configure Nginx (copy config to /etc/nginx/sites-available/)"
echo "4. Get SSL certificate: sudo certbot --nginx -d szybkie-wyzwania.pl"
echo "5. Deploy application!"
