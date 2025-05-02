import boto3
import csv
from pprint import pprint

# Create session
session = boto3.Session(profile_name="default")
aws_ec2_client = session.client("ec2", region_name="us-east-1")

# Get instance details
response = aws_ec2_client.describe_instances()

# Open CSV file
with open("ec2_instance_report.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Instance ID", "Launch Time", "Public IP"])

    # Extract info
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            launch_time = instance["LaunchTime"]
            public_ip = instance.get("PublicIpAddress", "N/A")

            # Optional: Print to console
            pprint(instance_id)

            # Write row to CSV
            writer.writerow([instance_id, launch_time, public_ip])

print("Instance details exported to ec2_instance_report.csv")

