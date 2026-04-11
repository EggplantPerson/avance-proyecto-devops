# DevOps AWS Project

## Descripción
Este proyecto implementa un flujo DevOps en AWS utilizando:

- GitHub (control de versiones)
- AWS CloudFormation (IaC)
- Docker (contenedores)
- AWS CodePipeline (CI/CD)
- AWS Systems Manager (despliegue)
- AWS CloudWatch (monitoreo)

## Estructura

- docker/: aplicación web y contenedores
- scripts/: automatización en bash
- aws/: infraestructura y despliegue
- python/: automatización con boto3

## Requisitos

- AWS CLI configurado
- Docker instalado
- Python 3 + boto3

## Uso

### 1. Crear infraestructura

```bash
aws cloudformation deploy \
--template-file aws/cloudformation.yaml \
--stack-name devops-stack