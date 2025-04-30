# Script to list EC2 instance ID , Instance Volume, Instance Image and lunch time

import boto3
from pprint import pprint
aws = boto3.session.Session(profile_name = "default")

aws_ec2 = aws.client(service_name = "ec2", region_name = "us-east-1")

# Using client object

ec2 = aws_ec2.describe_instances()
for item in ec2['Reservations']:
    for instance in item ['Instances']:
        print("The image Id is: {}\nThe Instance ID is :{}\n The instance Launch Time iS:{}".format(instance['ImageId'],instance['InstanceId'],instance['LaunchTime']))

# List the volume
response = aws_ec2.describe_volumes()['Volumes']
for item in response:
     print("The AvailabilityZone Id is: {}\nThe Instance ID is :{}\n The instance Launch Time iS:{}".format(item['AvailabilityZone'],item['VolumeType'],item['VolumeId']))
   
