#!/bin/bash
cd "$(dirname "$0")"
docker compose up -d
echo ""
echo "================================================="
echo " Odoo 19 sedang berjalan!"
echo " Buka browser di: http://localhost:8069"
echo "================================================="
