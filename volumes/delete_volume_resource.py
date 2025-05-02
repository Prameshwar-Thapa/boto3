import boto3

aws = boto3.session.Session(profile_name = "default")

aws_ec2_res = aws.resource(service_name = "ec2",region_name = "us-east-1")
# Filter to get available volume
f = {"Name":"status","Values":["available"]}
for each_volume in aws_ec2_res.volumes.filter(Filters=[f]):
# Volume which are available but with no tags
    if not each_volume.tags:
        print(each_volume.id,each_volume.state,each_volume.tags)
# Deleting unused and untagged volume
        print("Deleting unused and untagged Volumes.....")
        each_volume.delete()
print("Deleted all unused untagged volumes")
