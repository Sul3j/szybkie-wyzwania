#!/bin/bash
# Database backup script

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/opt/szybkie-wyzwania/backups"
CONTAINER_NAME="szybkie-wyzwania-db"
DB_NAME="${DB_NAME:-szybkie_wyzwania_prod}"
DB_USER="${DB_USER:-szybkie_wyzwania_user}"

mkdir -p $BACKUP_DIR

echo "💾 Creating database backup..."

# Backup database
docker exec $CONTAINER_NAME pg_dump -U $DB_USER $DB_NAME > $BACKUP_DIR/db_$DATE.sql

if [ $? -eq 0 ]; then
    # Compress
    gzip $BACKUP_DIR/db_$DATE.sql

    # Clean old backups (keep last 7 days)
    find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete

    echo "✅ Backup created: $BACKUP_DIR/db_$DATE.sql.gz"

    # Show backup size
    du -h $BACKUP_DIR/db_$DATE.sql.gz
else
    echo "❌ Backup failed!"
    exit 1
fi
