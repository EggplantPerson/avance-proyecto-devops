# Proyecto Devops AWS

## Descripción
Implementación de pipeline DevOps en AWS con automatización completa.

## Tecnologías
- AWS (EC2, S3, CloudFormation, CodePipeline)
- Docker
- Python (Boto3)
- Bash

## Funcionalidades
- Aprovisionamiento automático de infraestructura
- Contenerización de aplicación
- Pipeline CI/CD
- Monitoreo con CloudWatch

## Ejecución

### Scripts
bash scripts/setup.sh

### Docker
cd docker
docker build -t devops-app .
docker run -p 5000:5000 devops-app

### Python
python3 python/aws_script.py