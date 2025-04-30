# Returns details about the IAM user or role whose credentials are used to call the operation.

import boto3
aws = boto3.session.Session(profile_name = "default")

aws_caller = aws.client(service_name = "sts")

response = aws_caller.get_caller_identity()
print(response['Account'])

