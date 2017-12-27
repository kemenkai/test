import boto3
from botocore.exceptions import ClientError


# 查看VPC信息
def describe_instances(vpcid=None):
    try:
        session = boto3.Session(profile_name='default')
        session_ec2_client = session.client('ec2')

        response = session_ec2_client.describe_instances(
            Filters = [
                {
                    'Name': 'vpc-id',
                    'Values': [vpcid],
                }
            ]
        )

        print("{}".format(response))
        return response
    except ClientError as e:
        print(e)