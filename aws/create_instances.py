import boto3
from botocore.exceptions import ClientError
from aws import ami

# 创建新的服务器
def create_instances(HostName,Ip,security_group_id,subnetid,instancetype,ami=ami.amazon_ami,disk_size=100,public_ip_status=False,profile_name="default"):
    # session = boto3.Session(profile_name='kehu')
    session = boto3.Session(profile_name=profile_name)
    # session = boto3.Session(profile_name='bnbkr')
    session_ec2_client = session.client('ec2')
    session_ec2_resource = session.resource('ec2')

    try:
        if ami == ami.amazon_ami:
            response = session_ec2_resource.create_instances(
                # DryRun=True,
                BlockDeviceMappings = [
                    {
                        'DeviceName': '/dev/xvda',
                        'Ebs': {
                            # 'Encrypted': False,
                            'DeleteOnTermination': True,
                            # 'SnapshotId': 'snap-00f63af2b938a9ed8',
                            'VolumeSize': 40,
                            'VolumeType': 'gp2'
                        },
                    },
                    {
                        'DeviceName': '/dev/sdb',
                        'Ebs': {
                            # 'Encrypted': False,
                            'DeleteOnTermination': True,
                            'VolumeSize': disk_size,
                            'VolumeType': 'gp2'
                        },
                    }
                ],
                ImageId = ami,
                InstanceType = instancetype,
                KeyName = 'bnbJumpServerRoot',
                MaxCount = 1,
                MinCount = 1,
                Monitoring = {'Enabled': True},
                SecurityGroupIds = [security_group_id],
                SubnetId = subnetid,
                DisableApiTermination = True,
                # EbsOptimized = True,
                PrivateIpAddress = Ip,
                TagSpecifications = [
                    {
                        'ResourceType': 'volume',
                        'Tags': [{'Key': 'Name','Value': HostName}]},
                    {
                        'ResourceType': 'instance',
                        'Tags': [{'Key': 'Name', 'Value': HostName}]
                    }
                ]
            )

            print('{}服务器创建成功！！！'.format(HostName))
            print(response, HostName, Ip, security_group_id, subnetid, instancetype)
            return response,HostName,Ip,security_group_id,subnetid,instancetype
        elif ami == ami.win_2016:
            response = session_ec2_resource.create_instances(
                # DryRun=True,
                BlockDeviceMappings=[
                    {
                        'DeviceName': '/dev/xvda',
                        'Ebs': {
                            # 'Encrypted': False,
                            'DeleteOnTermination': True,
                            # 'SnapshotId': 'snap-00f63af2b938a9ed8',
                            'VolumeSize': disk_size,
                            'VolumeType': 'gp2'
                        },
                    },
                ],
                ImageId=ami,
                InstanceType=instancetype,
                KeyName='bnbJumpServerRoot',
                MaxCount=1,
                MinCount=1,
                Monitoring={'Enabled': True},
                SecurityGroupIds=[security_group_id],
                SubnetId=subnetid,
                DisableApiTermination=True,
                # EbsOptimized = True,
                PrivateIpAddress=Ip,
                TagSpecifications=[
                    {
                        'ResourceType': 'volume',
                        'Tags': [{'Key': 'Name', 'Value': HostName}]},
                    {
                        'ResourceType': 'instance',
                        'Tags': [{'Key': 'Name', 'Value': HostName}]
                    }
                ]
            )

            print('{}服务器创建成功！！！'.format(HostName))
            print(response, HostName, Ip, security_group_id, subnetid, instancetype)
            return response, HostName, Ip, security_group_id, subnetid, instancetype

        else:
            response = session_ec2_resource.create_instances(
                # DryRun=True,
                BlockDeviceMappings=[
                    # {
                    #     'DeviceName': '/dev/xvda',
                    #     'Ebs': {
                    #         # 'Encrypted': False,
                    #         'DeleteOnTermination': True,
                    #         # 'SnapshotId': 'snap-00f63af2b938a9ed8',
                    #         'VolumeSize': 40,
                    #         'VolumeType': 'gp2'
                    #     },
                    # },
                    {
                        'DeviceName': '/dev/sdb',
                        'Ebs': {
                            # 'Encrypted': False,
                            'DeleteOnTermination': True,
                            'VolumeSize': disk_size,
                            'VolumeType': 'gp2'
                        },
                    }
                ],
                ImageId=ami,
                InstanceType=instancetype,
                KeyName='bnbJumpServerRoot',
                MaxCount=1,
                MinCount=1,
                Monitoring={'Enabled': True},
                # SecurityGroupIds=[security_group_id],
                # SubnetId=subnetid,
                DisableApiTermination=True,
                # EbsOptimized = True,
                # PrivateIpAddress=Ip,
                NetworkInterfaces=[
                    {
                        'AssociatePublicIpAddress': public_ip_status,
                        'DeleteOnTermination': True,
                        # 'Description': 'publicIP',
                        'DeviceIndex': 0,
                        'PrivateIpAddress': Ip,
                        'SubnetId': subnetid,
                        'Groups': [security_group_id]
                    },
                ],
                TagSpecifications=[
                    {
                        'ResourceType': 'volume',
                        'Tags': [{'Key': 'Name', 'Value': HostName}]},
                    {
                        'ResourceType': 'instance',
                        'Tags': [{'Key': 'Name', 'Value': HostName}]
                    }
                ]
            )

            print('{}服务器创建成功！！！'.format(HostName))
            print(response[0],HostName,Ip,security_group_id,subnetid,instancetype)
            return response[0],HostName,Ip,security_group_id,subnetid,instancetype

    except ClientError as e:
        print('{}服务器创建失败！！！'.format(HostName))
        print('错误信息：\n {}'.format(e))