#!/bin/bash

echo "Actualizando sistema..."
sudo apt update -y

echo "Instalando dependencias..."
sudo apt install -y git docker.io python3 python3-pip

echo "Iniciando docker..."
sudo systemctl start docker

echo "Configuración completa"