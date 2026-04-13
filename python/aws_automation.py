import boto3
from datetime import datetime

ec2 = boto3.resource('ec2', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')

def crear_instancia():
    instances = ec2.create_instances(
        ImageId='ami-0ec10929233384c7f',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    print("Instancia creada:", instances[0].id)

def listar_ec2():
    data = []

    for instance in ec2.instances.all():
        info = {
            "ID": instance.id,
            "Estado": instance.state['Name'],
            "Tipo": instance.instance_type
        }
        print(info)
        data.append(info)

    return data    

def listar_s3():

    buckets = s3.list_buckets()
    data = []

    for b in buckets['Buckets']:
        nombre = b['Name']
        print(f"\nBucket: {nombre}")

        objetos = s3.list_objects_v2(Bucket=nombre)

        lista_objetos = []

        if 'Contents' in objetos:
            for obj in objetos['Contents']:
                print(f"  - {obj['Key']}")
                lista_objetos.append(obj['Key'])
        else:
            print("  (vacío)")

        data.append({
            "Bucket": nombre,
            "Objetos": lista_objetos
        })

    return data

def generar_reporte(ec2_data, s3_data):
    nombre = f"reporte_aws_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(nombre, "w") as f:
        f.write("==== REPORTE AWS ====\n\n")

        f.write("EC2 INSTANCES:\n")
        for i in ec2_data:
            f.write(str(i) + "\n")

        f.write("\nS3 BUCKETS:\n")
        for b in s3_data:
            f.write(str(b) + "\n")

    print(f"\n Reporte generado: {nombre}")

if __name__ == "__main__":
    crear_instancia()

    ec2_data = listar_ec2()
    s3_data = listar_s3()

    generar_reporte(ec2_data, s3_data)