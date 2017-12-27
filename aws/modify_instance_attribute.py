import boto3
from botocore.exceptions import ClientError

# 修改终止保护状态True：不可以终止服务器，Fales：可以终止服务器
def modify_instance_attribute(instanceid=None,status=True):
    try:

        session = boto3.Session(profile_name='default')
        session_ec2_client = session.client('ec2')

        response = session_ec2_client.modify_instance_attribute(
            InstanceId = instanceid,
            DisableApiTermination = {
                'Value': status
            }
        )

        print(response)
    except ClientError as e:
        print(e)

# modify_instance_attribute(instanceid="i-0d2b8c5db4fbb2708",status=False)
# modify_instance_attribute(instanceid="i-0575ea20281427039",status=False)