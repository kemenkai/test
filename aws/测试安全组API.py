import boto3
from botocore.exceptions import ClientError
import time


session = boto3.Session(profile_name='kehu')
session_ec2 = session.client('ec2')
session_ec2_resource = session.resource('ec2')

#ec2 = boto3.client('ec2', role_arn='kehu')
# response = session_ec2.describe_regions()
# print(response['Regions'])
# response = session_ec2.describe_availability_zones()
# print(response['AvailabilityZones'])

# try:
#     response = session_ec2.describe_security_groups(GroupIds=['sg-53c1cb35'])
#     print(response)
# except ClientError as e:
#     print(e)

response = session_ec2.describe_vpcs()
vpc_tag = response.get('Vpcs', [{}])[0].get('Tags', [{}])[0].get('Value','')
vpc_id = response.get('Vpcs', [{}])[1].get('VpcId', '')

try:
    # 创建 office 安全组
    office_security_group = session_ec2.create_security_group(
        GroupName = 'zqlPublicOffice',
        Description = 'zqlPublicOffice',
        VpcId = vpc_id
    )
    office_security_group_id = office_security_group['GroupId']
    office_security_group_resource = session_ec2_resource.SecurityGroup(office_security_group_id)
    office_security_group_resource.create_tags(
        Tags=[{
            'Key': 'Name',
            'Value': 'zqlOffice'}])
    print('VPC"{1}"中Office安全组创建成功.\n 安全组ID：{0}'.format(office_security_group_id, vpc_tag))

    # 创建 Private 安全组
    private_security_group = session_ec2.create_security_group(
        GroupName = 'zqlPrivate',
        Description = 'zqlPrivate',
        VpcId = vpc_id
    )
    private_security_group_id = private_security_group['GroupId']
    private_security_group_resource = session_ec2_resource.SecurityGroup(private_security_group_id)
    private_security_group_resource.create_tags(
        Tags=[{
            'Key': 'Name',
            'Value': 'zqlPrivate'}])
    print('VPC"{1}"中Private安全组创建成功.\n 安全组ID：{0}'.format(private_security_group_id, vpc_tag))

    # 创建 PublicAll 安全组
    public_security_group = session_ec2.create_security_group(
        GroupName = 'zqlPublicAll',
        Description = 'zqlPublicAll',
        VpcId = vpc_id
    )
    public_security_group_id = public_security_group['GroupId']
    public_security_group_resource = session_ec2_resource.SecurityGroup(public_security_group_id)
    public_security_group_resource.create_tags(
        Tags=[{
            'Key': 'Name',
            'Value': 'zqlPublicAll'}])
    print('VPC"{1}"中Public安全组创建成功.\n 安全组ID：{0}'.format(public_security_group_id, vpc_tag))

    # 创建 resourceStatic 安全组
    resource_security_group = session_ec2.create_security_group(
        GroupName = 'zqlResourceStatic',
        Description = 'zqlResourceStatic',
        VpcId = vpc_id
    )
    resource_security_group_id = resource_security_group['GroupId']
    resource_security_group_resource = session_ec2_resource.SecurityGroup(resource_security_group_id)
    resource_security_group_resource.create_tags(
        Tags=[{
            'Key': 'Name',
            'Value': 'zqlResource'}])
    print('VPC"{1}"中Resource安全组创建成功.\n 安全组ID：{0}'.format(resource_security_group_id, vpc_tag))

###################################################################################################################

    # 添加 Office 安全组策略
    office_security_group_data = session_ec2.authorize_security_group_ingress(
        GroupId = '{}'.format(str(office_security_group_id)),
        IpPermissions = [
            {'IpProtocol': '-1',
             'ToPort': -1,
             'IpRanges': [{'Description': 'Office', 'CidrIp': '180.168.91.190/32'}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'IpRanges': [{'Description': 'MasterServer', 'CidrIp': '172.16.255.0/24'}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicOffice', 'GroupId': office_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublic', 'GroupId': public_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPrivate', 'GroupId': private_security_group_id}]}
        ])
    print('安全组规则添加信息{}'.format(office_security_group_data))

    # 添加 ResourceStatic 安全组策略
    resource_security_group_data = session_ec2.authorize_security_group_ingress(
        GroupId = resource_security_group_id,
        IpPermissions = [
            {'IpProtocol': '-1',
             'ToPort': -1,
             'IpRanges': [{'Description': 'MasterServer', 'CidrIp': '172.16.255.0/24'}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicOffice', 'GroupId': office_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPrivate', 'GroupId': private_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicAll', 'GroupId': public_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlResource', 'GroupId': resource_security_group_id}]},
            {'IpProtocol': 'tcp',
             'ToPort': 80,
             'FromPort': 80,
             'IpRanges': [{'Description': 'Http', 'CidrIp': '0.0.0.0/0'}]}
        ])
    print('安全组规则添加信息{}'.format(resource_security_group_data))

    # 添加 Private 安全组策略
    private_security_group_data = session_ec2.authorize_security_group_ingress(
        GroupId = private_security_group_id,
        IpPermissions = [
            {'IpProtocol': '-1',
             'ToPort': -1,
             'IpRanges': [{'Description': 'MasterServer', 'CidrIp': '172.16.255.0/24'}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicOffice', 'GroupId': office_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPrivate', 'GroupId': private_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicAll', 'GroupId': public_security_group_id}]}
        ])
    print('安全组规则添加信息{}'.format(private_security_group_data))

    # 添加 PublicAll 安全组策略
    public_security_group_data = session_ec2.authorize_security_group_ingress(
        GroupId = public_security_group_id,
        IpPermissions = [
            {'IpProtocol': '-1',
             'ToPort': -1,
             'IpRanges': [{'Description': 'MasterServer', 'CidrIp': '172.16.255.0/24'}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicOffice', 'GroupId': office_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPrivate', 'GroupId': private_security_group_id}]},
            {'IpProtocol': '-1',
             'ToPort': -1,
             'UserIdGroupPairs': [{'Description': 'zqlPublicAll', 'GroupId': public_security_group_id}]},
            {'IpProtocol': 'tcp',
             'ToPort': 80,
             'FromPort': 80,
             'UserIdGroupPairs': [{'Description': 'zqlResource', 'GroupId': resource_security_group_id}]},
            {'IpProtocol': 'tcp',
             'ToPort': 80,
             'FromPort': 80,
             'IpRanges': [{'Description': 'Http', 'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'ToPort': 443,
             'FromPort': 443,
             'IpRanges': [{'Description': 'Https', 'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'ToPort': 9443,
             'FromPort': 9443,
             'IpRanges': [{'Description': 'Wss', 'CidrIp': '0.0.0.0/0'}]},
        ])
    print('安全组规则添加信息{}'.format(public_security_group_data))

except ClientError as e:
    # Delete security group
    try:
        response = session_ec2.delete_security_group(GroupId='{}'.format(office_security_group_id))
        print('{}安全组删除成功！！'.format(office_security_group_id))
        response = session_ec2.delete_security_group(GroupId='{}'.format(private_security_group_id))
        print('{}安全组删除成功！！'.format(private_security_group_id))
        response = session_ec2.delete_security_group(GroupId='{}'.format(public_security_group_id))
        print('{}安全组删除成功！！'.format(public_security_group_id))
        response = session_ec2.delete_security_group(GroupId='{}'.format(resource_security_group_id))
        print('{}安全组删除成功！！'.format(resource_security_group_id))
    except ClientError as e:
        print(e)
    print(e)



# # Delete security group
# try:
#     print(security_group_id)
#     response = session_ec2.delete_security_group(GroupId='{}'.format(security_group_id))
#     print('安全组删除成功！！'.format(security_group_id))
# except ClientError as e:
#     print(e)