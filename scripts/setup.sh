#!/bin/bash

echo "Actualizando sistema..."
sudo apt update

echo "Instalando paquetes..."
sudo apt install -y git docker.io python3 python3-pip

echo "Activando docker..."
sudo systemctl start docker
sudo systemctl enable docker

echo "Agregando usuario al grupo docker..."
sudo usermod -aG docker $USER

echo "Setup completado"