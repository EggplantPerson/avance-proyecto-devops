import boto3
from datetime import datetime

ec2 = boto3.resource('ec2')
s3 = boto3.client('s3')

def create_instance():
    print("Creando instancia EC2...")
    instances = ec2.create_instances(
        ImageId='ami-0c02fb55956c7d316',  # Ubuntu (puede cambiar según región)
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    print(f"Instancia creada: {instances[0].id}")

def list_buckets():
    print("\nBuckets S3:")
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

def generate_report():
    now = datetime.now()
    with open("reporte.txt", "w") as f:
        f.write(f"Reporte generado: {now}\n")
        f.write("Instancias EC2 y buckets listados.\n")

if __name__ == "__main__":
    create_instance()
    list_buckets()
    generate_report()