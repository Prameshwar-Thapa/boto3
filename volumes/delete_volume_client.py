import boto3

aws = boto3.session.Session(profile_name = "default")

aws_ec2 = aws.client(service_name = "ec2", region_name = "us-east-1")
# Avaliable volume without tags
response =  aws_ec2.describe_volumes()['Volumes']
for each_item in response:
    if not "Tags" in each_item and each_item['State']=='available':
        print('Deleting',each_item['VolumeId'])
        aws_ec2.delete_volume(VolumeId=each_item['VolumeId'])
print("Delete all unused and untagged volume")
        

