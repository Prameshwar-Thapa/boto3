import boto3
from pprint import pprint

aws = boto3.session.Session(profile_name = "default")

aws_ec2_resource = aws.resource(service_name = "ec2", region_name = "us-east-1")
aws_ec2_client = aws.client(service_name = "ec2", region_name = "us-east-1")

# Using Resource

response = aws_ec2_resource.instances.all()
for instance in response:
    print(instance.id)

# Usign Clients

client = aws_ec2_client.describe_instances()
for item in client['Reservations']:
    for instance in item['Instances']:
        pprint(instance['InstanceId'])

