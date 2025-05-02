import boto3

aws = boto3.session.Session(profile_name = "default")

aws_ec2 = aws.resource(service_name = "ec2", region_name = "us-east-1")

f1 = {"Name": "instance-state-name","Values":["stopped","running"]}
f2 = {"Name": "instance-type","Values":["t2.micro"]}

response = aws_ec2.instances.filter(Filters=[f1,f2])
for item in response:
    print(item)
