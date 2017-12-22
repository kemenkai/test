import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='kehu')
session_ec2 = session.resource('ec2')
security_group = session_ec2.SecurityGroup('sg-ed799194')
security_group.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'zqlPublicAll'
        }
    ]
)


# try:
#     response = session_ec2.update_security_group_rule_descriptions_egress(
#         GroupId='sg-ed799194',
#
#     )
# except ClientError as e:
#     print(e)