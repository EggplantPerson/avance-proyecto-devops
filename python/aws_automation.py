import boto3

ec2 = boto3.resource('ec2')
s3 = boto3.client('s3')

def crear_instancia():
    instances = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    print("Instancia creada:", instances[0].id)

def listar_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print("Bucket:", bucket['Name'])

if __name__ == "__main__":
    crear_instancia()
    listar_buckets()