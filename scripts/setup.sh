#!/bin/bash

echo "Actualizando sistema..."
sudo apt update

echo "Instalando dependencias..."
sudo apt install git docker.io python3 python3-pip -y

echo "Iniciando docker..."
sudo systemctl start docker
sudo systemctl enable docker

echo "Configuración completa"