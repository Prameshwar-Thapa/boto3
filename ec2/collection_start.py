import boto3

aws = boto3.session.Session(profile_name = "default")

# Creating resource and Client
aws_ec2 = aws.resource(service_name = "ec2", region_name = "us-east-1")
aws_ec2_client = aws.client(service_name = "ec2", region_name = "us-east-1")

# Collecting the Instance Ids
'''
all_instance_ids = []
for each in aws_ec2.instances.all():
    all_instance_ids.append(each.id)


waiter = aws_ec2_client.get_waiter('instance_running')
aws_ec2.instances.start()
waiter.wait(InstanceIds=all_instance_ids)
print("your all instacne are up and running")
'''
# Collecting the Non_prod Instances Using Resource and collector objects
'''
np_sers_ids=[]
f1= {'Name': 'tag:Name','Values': ['Non_prod']}

for each_in in aws_ec2.instances.filter(Filters=[f1]):
    np_sers_ids.append(each_in.id)
print(np_sers_ids)
print("--------------------------------")
'''

# Collecting Non_Prdo Instances using Client and filter
f1= {'Name': 'tag:Name','Values': ['Non_prod']}
np_sers_ids=[]
for each_item in aws_ec2_client.describe_instances(Filters=[f1])['Reservations']:
    for each_in in each_item['Instances']:
        np_sers_ids.append(each_in['InstanceId'])
    print(np_sers_ids)
print("starting instances with the ids of:", np_sers_ids)
aws_ec2_client.start_instances(InstanceIds=np_sers_ids)
waiter = aws_ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=np_sers_ids)
print("Your np instance are up and running...")


