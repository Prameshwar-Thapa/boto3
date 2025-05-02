import boto3

aws = boto3.session.Session(profile_name = "default")
aws_ec2 = aws.client(service_name = "ec2", region_name = "us-east-1")

sts = aws.client(service_name = "sts",region_name = "us-east-1")
sts_id = sts.get_caller_identity()
my_own_id = sts_id.get('Account')

response = aws_ec2.describe_snapshots(OwnerIds = [my_own_id])
for each in response['Snapshots']:
    print(each['SnapshotId'])

