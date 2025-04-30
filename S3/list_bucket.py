import boto3
from pprint import pprint

aws = boto3.session.Session(profile_name = "default")

aws_s3_resource = aws.resource(service_name = "s3")
aws_s3_client = aws.client(service_name = "s3")

# Using Resource

response = aws_s3_resource.buckets.all()
for bucket in response:
    print(bucket.name)

# Using Client

client = aws_s3_client.list_buckets()
for bucket in client['Buckets']:
    print(bucket['Name'])

