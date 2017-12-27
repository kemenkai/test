import boto3
from botocore.exceptions import ClientError


# 终止服务器
def terminate_instances(instancesid=None):
    try:
        session = boto3.Session(profile_name='default')
        session_ec2_client = session.client('ec2')

        response = session_ec2_client.terminate_instances(

            InstanceIds = [
                instancesid
            ]
        )

        print(response)

    except ClientError as e:
        print(e)

# modify_instance_attribute(instanceid="i-03e34f6c144b2e07a",status=False)
# terminate_instances(instancesid='i-03e34f6c144b2e07a')