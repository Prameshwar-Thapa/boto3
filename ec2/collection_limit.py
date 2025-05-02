import boto3

aws = boto3.session.Session(profile_name = "default")
aws_ec2 = aws.resource(service_name = "ec2", region_name = "us-east-1")
# Listing only 2 Instances
response = aws_ec2.instances.limit(2)
for item in response:
    print(item)
