import boto3

aws = boto3.session.Session(profile_name = "default")
aws_ec2 = aws.resource(service_name = "ec2", region_name = "us-east-1")

# List all lists of ec2 in us-east-1
response = aws_ec2.instances.all()
for item in response:
    print(item)
