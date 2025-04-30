import boto3


aws = boto3.session.Session(profile_name = "default")

aws_iam_res = aws.resource(service_name = "iam")
aws_iam_client = aws.client(service_name = "iam")

response = aws_iam_res.users.all()
for user in response:
    print(user.name)

client = aws_iam_client.list_users()
for user in client['Users']:
    print(user['UserName'])
