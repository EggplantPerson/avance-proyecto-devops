#!/bin/bash

echo "Limpiando logs..."
sudo find /var/log -type f -name "*.log" -delete

echo "Logs eliminados correctamente"