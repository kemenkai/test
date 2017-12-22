# -*- coding: UTF-8 -*-
import boto3
from botocore.exceptions import ClientError
import time


# 0 : pending
# 16 : running
# 32 : shutting-down
# 48 : terminated
# 64 : stopping
# 80 : stopped

bnb_tokyo_vpc_id = 'vpc-08281e6c'

web_a = 'subnet-2ea32367'
web_c = 'subnet-3f6d9464'
rds_a = 'subnet-a8ac2ce1'
rds_c = 'subnet-0f6a9354'
alb_a = 'subnet-abae2ee2'
alb_c = 'subnet-836891d8'
mbx_a = 'subnet-50ab2b19'
mbx_c = 'subnet-066f965d'
block_a = 'subnet-1cad2d55'
network_inout = 'subnet-c7ae2e8e'
log_a = 'subnet-60a22929'
log_c = 'subnet-86c808dd'
bnb_mbx_a = 'subnet-79fe3230'
bnb_mbx_c = 'subnet-b93938e1'
bnb_blcok_nat = 'subnet-5b53ff12'
bnb_blcok_all = 'subnet-8523c4de'
bnb_test = 'subnet-a4ea41ed'
bnb_launchpad_a = 'subnet-2abc2c63'
bnb_launchpad_c = 'subnet-397ab462'
bnb_kr_vpn1 = 'subnet-04d40d6c'
bnb_kr_vpn2 = 'subnet-7846b534'
bnb_mkm_a = 'subnet-48c1a401'
bnb_mkm_c = 'subnet-2a26f571'


private_security_group_id = 'sg-128e646b'
public_security_group_id = 'sg-dd8c66a4'
office_security_group_id = 'sg-958f65ec'
resource_security_group_id = 'sg-478a603e'
bnb_office_security_group_id = 'sg-8adf98ec'
bnb_public_security_group_id = 'sg-76de9910'
bnb_private_security_group_id = 'sg-c3d295a5'
bnb_kr_public_security_group_id = 'sg-86e34ced'

amazon_ami = 'ami-2803ac4e'
http_ami = 'ami-23a16245'
wss_ami = 'ami-bffd39d9'
ubuntu16_ami = 'ami-050bcf63'
centos7_ami = 'ami-8405c1e2'
btc_ami = 'ami-1011cb76'
omn_ami = 'ami-a853e1ce'
eth_ami = 'ami-c410b8a2'
kr_proxy_ami = 'ami-3d62c453'
win_2016 = 'ami-4325fa25'
mkm_ami = 'ami-2ef47c48'
zookeeper_ami = 'ami-d72ea5b1'


# 创建新的服务器
def create_instances(HostName,Ip,security_group_id,subnetid,instancetype,ami=amazon_ami,disk_size=100,public_ip_status=False):
    # session = boto3.Session(profile_name='kehu')
    session = boto3.Session(profile_name='default')
    # session = boto3.Session(profile_name='bnbkr')
    session_ec2_client = session.client('ec2')
    session_ec2_resource = session.resource('ec2')

    try:

        if ami == amazon_ami:
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
        elif ami == win_2016:
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
            # response = session_ec2_resource.create_instances(
            #     # DryRun=True,
            #     BlockDeviceMappings=[
            #         # {
            #         #     'DeviceName': '/dev/xvda',
            #         #     'Ebs': {
            #         #         # 'Encrypted': False,
            #         #         'DeleteOnTermination': True,
            #         #         # 'SnapshotId': 'snap-00f63af2b938a9ed8',
            #         #         'VolumeSize': 40,
            #         #         'VolumeType': 'gp2'
            #         #     },
            #         # },
            #         {
            #             'DeviceName': '/dev/sdb',
            #             'Ebs': {
            #                 # 'Encrypted': False,
            #                 'DeleteOnTermination': True,
            #                 'VolumeSize': disk_size,
            #                 'VolumeType': 'gp2'
            #             },
            #         }
            #     ],
            #     ImageId=ami,
            #     InstanceType=instancetype,
            #     KeyName='bnbJumpServerRoot',
            #     MaxCount=1,
            #     MinCount=1,
            #     Monitoring={'Enabled': True},
            #     SecurityGroupIds=[security_group_id],
            #     SubnetId=subnetid,
            #     DisableApiTermination=True,
            #     # EbsOptimized = True,
            #     PrivateIpAddress=Ip,
            #     TagSpecifications=[
            #         {
            #             'ResourceType': 'volume',
            #             'Tags': [{'Key': 'Name', 'Value': HostName}]},
            #         {
            #             'ResourceType': 'instance',
            #             'Tags': [{'Key': 'Name', 'Value': HostName}]
            #         }
            #     ]
            # )
            #
            # print('{}服务器创建成功！！！'.format(HostName))
            # print(response[0],HostName,Ip,security_group_id,subnetid,instancetype)
            # return response[0],HostName,Ip,security_group_id,subnetid,instancetype
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



host = {'web1':{'HostName':'Web1','ip':'1.11','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
        'web2':{'HostName':'Web2','ip':'2.11','GroupId':office_security_group_id,'SubnetId':web_c,'instancetype':'m4.xlarge'},
        'admin_pnk':{'HostName':'AdminPnk','ip':'1.40','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
        'admin_ex':{'HostName':'AdminEx','ip':'1.41','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
        'stream1':{'HostName':'Stream1','ip':'1.50','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
        'stream2':{'HostName':'Stream2','ip':'2.50','GroupId':office_security_group_id,'SubnetId':web_c,'instancetype':'m4.xlarge'},
        'file':{'HostName':'File','ip':'1.49','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
        'mongo':{'HostName':'Mongo','ip':'1.100','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'c4.xlarge'},
        'chat':{'HostName':'Chat','ip':'1.110','GroupId':public_security_group_id,'SubnetId':web_a,'instancetype':'c4.xlarge'},
        'resource':{'HostName':'Resource','ip':'1.250','GroupId':public_security_group_id,'SubnetId':web_a,'instancetype':'c4.xlarge'},
        'eng1':{'HostName':'MbxEng1','ip':'10.10','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.xlarge'},
        'eng2':{'HostName':'MbxEng2','ip':'11.10','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.xlarge'},
        'eng3':{'HostName':'MbxEng3','ip':'10.11','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.xlarge'},
        'mgmt1':{'HostName':'MbxMgmt1','ip':'10.20','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'c4.2xlarge'},
        'mgmt2':{'HostName':'MbxMgmt2','ip':'11.20','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'c4.2xlarge'},
        'priv1':{'HostName':'MbxPriv1','ip':'10.30','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'priv2':{'HostName':'MbxPriv2','ip':'11.30','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'rest1':{'HostName':'MbxRest1','ip':'10.40','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'c4.2xlarge'},
        'rest2':{'HostName':'MbxRest2','ip':'11.40','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'c4.2xlarge'},
        'pub1':{'HostName':'MbxPub1','ip':'10.50','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'pub2':{'HostName':'MbxPub1','ip':'11.50','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'kline1':{'HostName':'MbxKline1','ip':'10.60','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'kline2':{'HostName':'MbxKline2','ip':'11.60','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'user1':{'HostName':'MbxUser1','ip':'10.70','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'agg1':{'HostName':'MbxAggTrade1','ip':'10.80','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'agg2':{'HostName':'MbxAggTrade2','ip':'11.80','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'rmqint1':{'HostName':'MbxRmqInt1','ip':'10.90','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'rmqint2':{'HostName':'MbxRmqInt2','ip':'11.90','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'rmqout1':{'HostName':'MbxRmqOut1','ip':'10.100','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'rmqout2':{'HostName':'MbxRmqOut2','ip':'11.100','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'rmqha1':{'HostName':'MbxRmqHa1','ip':'10.110','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'rmqha2':{'HostName':'MbxRmqHa2','ip':'11.110','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'http1':{'HostName':'MbxHttp1','ip':'10.120','GroupId':public_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
        'http2':{'HostName':'MbxHttp2','ip':'11.120','GroupId':public_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
        'wss1':{'HostName':'MbxWss1','ip':'10.130','GroupId':public_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.large'},
        'wss2':{'HostName':'MbxWss2','ip':'11.130','GroupId':public_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.large'},
        }

# create_instances('bnbDockerServer','172.16.255.15','sg-8adf98ec','subnet-01fc3048','m4.xlarge',ami='ami-050bcf63',disk_size=1024)
# create_instances('Testaaaaa','172.16.255.20','sg-8adf98ec','subnet-01fc3048','m4.xlarge')
# create_instances(host['web1']['HostName'],host['web1']['ip'],host['web1']['GroupId'],host['web1']['SubnetId'],host['web1']['instancetype'])
# create_instances(host['web2']['HostName'],host['web2']['ip'],host['web2']['GroupId'],host['web2']['SubnetId'],host['web2']['instancetype'])
# create_instances(host['admin_pnk']['HostName'], host['admin_pnk']['ip'], host['admin_pnk']['GroupId'],host['admin_pnk']['SubnetId'], host['admin_pnk']['instancetype'])
# create_instances(host['admin_ex']['HostName'], host['admin_ex']['ip'], host['admin_ex']['GroupId'],host['admin_ex']['SubnetId'], host['admin_ex']['instancetype'])
# create_instances(host['stream1']['HostName'],host['stream1']['ip'],host['stream1']['GroupId'],host['stream1']['SubnetId'],host['stream1']['instancetype'])
# create_instances(host['stream2']['HostName'],host['stream2']['ip'],host['stream2']['GroupId'],host['stream2']['SubnetId'],host['stream2']['instancetype'])
# create_instances(host['file']['HostName'],host['file']['ip'],host['file']['GroupId'],host['file']['SubnetId'],host['file']['instancetype'])
# create_instances(host['mongo']['HostName'],host['mongo']['ip'],host['mongo']['GroupId'],host['mongo']['SubnetId'],host['mongo']['instancetype'],ami=centos7_ami,disk_size=1024)
# create_instances(host['chat']['HostName'],host['chat']['ip'],host['chat']['GroupId'],host['chat']['SubnetId'],host['chat']['instancetype'],ami=wss_ami,disk_size=1024)
# create_instances(host['resource']['HostName'],host['resource']['ip'],host['resource']['GroupId'],host['resource']['SubnetId'],host['resource']['instancetype'],disk_size=100)
# create_instances(host['eng1']['HostName'],host['eng1']['ip'],host['eng1']['GroupId'],host['eng1']['SubnetId'],host['eng1']['instancetype'],disk_size=1024)
# create_instances(host['eng2']['HostName'],host['eng2']['ip'],host['eng2']['GroupId'],host['eng2']['SubnetId'],host['eng2']['instancetype'],disk_size=1024)
# create_instances(host['eng3']['HostName'],host['eng3']['ip'],host['eng3']['GroupId'],host['eng3']['SubnetId'],host['eng3']['instancetype'],disk_size=1024)
# create_instances(host['mgmt1']['HostName'],host['mgmt1']['ip'],host['mgmt1']['GroupId'],host['mgmt1']['SubnetId'],host['mgmt1']['instancetype'],disk_size=1024)
# create_instances(host['mgmt2']['HostName'],host['mgmt2']['ip'],host['mgmt2']['GroupId'],host['mgmt2']['SubnetId'],host['mgmt2']['instancetype'],disk_size=1024)
# create_instances(host['priv1']['HostName'],host['priv1']['ip'],host['priv1']['GroupId'],host['priv1']['SubnetId'],host['priv1']['instancetype'],disk_size=1024)
# create_instances(host['priv2']['HostName'],host['priv2']['ip'],host['priv2']['GroupId'],host['priv2']['SubnetId'],host['priv2']['instancetype'],disk_size=1024)
# create_instances(host['rest1']['HostName'],host['rest1']['ip'],host['rest1']['GroupId'],host['rest1']['SubnetId'],host['rest1']['instancetype'],disk_size=1024)
# create_instances(host['rest2']['HostName'],host['rest2']['ip'],host['rest2']['GroupId'],host['rest2']['SubnetId'],host['rest2']['instancetype'],disk_size=1024)
# create_instances(host['pub1']['HostName'],host['pub1']['ip'],host['pub1']['GroupId'],host['pub1']['SubnetId'],host['pub1']['instancetype'],disk_size=1024)
# create_instances(host['pub2']['HostName'],host['pub2']['ip'],host['pub2']['GroupId'],host['pub2']['SubnetId'],host['pub2']['instancetype'],disk_size=1024)
# create_instances(host['kline1']['HostName'],host['kline1']['ip'],host['kline1']['GroupId'],host['kline1']['SubnetId'],host['kline1']['instancetype'],disk_size=1024)
# create_instances(host['kline2']['HostName'],host['kline2']['ip'],host['kline2']['GroupId'],host['kline2']['SubnetId'],host['kline2']['instancetype'],disk_size=1024)
# create_instances(host['user1']['HostName'],host['user1']['ip'],host['user1']['GroupId'],host['user1']['SubnetId'],host['user1']['instancetype'],disk_size=1024)
# create_instances(host['agg1']['HostName'],host['agg1']['ip'],host['agg1']['GroupId'],host['agg1']['SubnetId'],host['agg1']['instancetype'],disk_size=1024)
# create_instances(host['agg2']['HostName'],host['agg2']['ip'],host['agg2']['GroupId'],host['agg2']['SubnetId'],host['agg2']['instancetype'],disk_size=1024)
# create_instances(host['rmqint1']['HostName'],host['rmqint1']['ip'],host['rmqint1']['GroupId'],host['rmqint1']['SubnetId'],host['rmqint1']['instancetype'],disk_size=100)
# create_instances(host['rmqint2']['HostName'],host['rmqint2']['ip'],host['rmqint2']['GroupId'],host['rmqint2']['SubnetId'],host['rmqint2']['instancetype'],disk_size=100)
# create_instances(host['rmqout1']['HostName'],host['rmqout1']['ip'],host['rmqout1']['GroupId'],host['rmqout1']['SubnetId'],host['rmqout1']['instancetype'],disk_size=100)
# create_instances(host['rmqout2']['HostName'],host['rmqout2']['ip'],host['rmqout2']['GroupId'],host['rmqout2']['SubnetId'],host['rmqout2']['instancetype'],disk_size=100)
# create_instances(host['rmqha1']['HostName'],host['rmqha1']['ip'],host['rmqha1']['GroupId'],host['rmqha1']['SubnetId'],host['rmqha1']['instancetype'],disk_size=100)
# create_instances(host['rmqha2']['HostName'],host['rmqha2']['ip'],host['rmqha2']['GroupId'],host['rmqha2']['SubnetId'],host['rmqha2']['instancetype'],disk_size=100)
# create_instances(host['http1']['HostName'],host['http1']['ip'],host['http1']['GroupId'],host['http1']['SubnetId'],host['http1']['instancetype'],disk_size=1024)
# create_instances(host['http2']['HostName'],host['http2']['ip'],host['http2']['GroupId'],host['http2']['SubnetId'],host['http2']['instancetype'],disk_size=1024)
# create_instances(host['wss1']['HostName'],host['wss1']['ip'],host['wss1']['GroupId'],host['wss1']['SubnetId'],host['wss1']['instancetype'],disk_size=1024)
# create_instances(host['wss2']['HostName'],host['wss2']['ip'],host['wss2']['GroupId'],host['wss2']['SubnetId'],host['wss2']['instancetype'],disk_size=1024)
# create_instances('Test','172.16.255.50','sg-8adf98ec','subnet-01fc3048','t2.large')

# 区块链服务器购买
# create_instances('bnbBTG','172.16.5.10','sg-8adf98ec','subnet-5b53ff12','m4.4xlarge')
# create_instances('bnbNEBL','172.16.5.11',bnb_office_security_group_id,bnb_blcok_nat,'c4.xlarge',ami=centos7_ami,disk_size=1024)



# Log服务器购买
# create_instances('bnbLog1','172.16.11.10','sg-8adf98ec',log_c,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog2','172.16.12.10','sg-8adf98ec',log_c,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog3','172.16.11.11','sg-8adf98ec',log_a,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog4','172.16.12.11','sg-8adf98ec',log_c,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog5','172.16.11.12','sg-8adf98ec',log_a,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog6','172.16.12.12','sg-8adf98ec',log_c,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog7','172.16.11.13','sg-8adf98ec',log_a,'i3.8xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog8','172.16.11.14','sg-8adf98ec',log_a,'r4.4xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog9','172.16.12.14','sg-8adf98ec',log_c,'r4.4xlarge',ami='ami-ce239fa8',)
# create_instances('bnbLog10','172.16.11.15','sg-8adf98ec',log_a,'r4.4xlarge',ami='ami-ce239fa8',)

# Mkm服务器购买
create_instances('bnbMkm1','172.16.13.11',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm2','172.16.14.11',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm3','172.16.13.12',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm4','172.16.14.12',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm5','172.16.13.13',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm6','172.16.14.13',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm7','172.16.13.14',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm8','172.16.14.14',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm9','172.16.13.15',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbMkm10','172.16.14.15',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
create_instances('bnbZookeeper1','172.16.13.250',bnb_office_security_group_id,bnb_mkm_a,'t2.xlarge',ami=zookeeper_ami)

# 临时购买服务器
# create_instances('Test','172.16.0.100',bnb_office_security_group_id,bnb_test,'t2.2xlarge',ami=win_2016)
# create_instances('bnbWAVES','172.16.5.13',bnb_office_security_group_id,bnb_blcok_nat,'m4.xlarge',ami=ubuntu16_ami,disk_size=500)








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

# describe_instances(vpcid=bnb_tokyo_vpc_id)

# modify_instance_attribute(instanceid='i-0c11cfe44c09e0ac8',status=False)
# aaa = describe_instances(vpcid='vpc-08281e6c')
#
# for num in range(len(aaa['Reservations'])):
#     bbb = aaa['Reservations'][num]['Instances'][0]['Tags'][0]['Value']
#
#     if 'Mbx' in bbb:
#         print(bbb)
#
# if 'Mbx' in aaa:
#     print(aaa)


# session = boto3.Session(profile_name='kehu')
# session_ec2_client = session.client('ec2')
# session_ec2_resource = session.resource('ec2')
#
# web_a = 'subnet-2ea32367'
# web_c = 'subnet-3f6d9464'
# rds_a = 'subnet-a8ac2ce1'
# rds_c = 'subnet-0f6a9354'
# alb_a = 'subnet-abae2ee2'
# alb_c = 'subnet-836891d8'
# mbx_a = 'subnet-50ab2b19'
# mbx_c = 'subnet-066f965d'
# block_a = 'subnet-1cad2d55'
# network_inout = 'subnet-c7ae2e8e'
#
# private_group_id = 'sg-128e646b'
# public_group_id = 'sg-dd8c66a4'
# office_group_id = 'sg-958f65ec'
# resource_group_id = 'sg-478a603e'
#
# try:
#     response = session_ec2_resource.create_instances(
#         # DryRun=True,
#         BlockDeviceMappings=[
#             {
#                 'DeviceName': '/dev/xvda',
#                 'Ebs': {
#                     # 'Encrypted': False,
#                     'DeleteOnTermination': True,
#                     # 'SnapshotId': 'snap-00f63af2b938a9ed8',
#                     'VolumeSize': 40,
#                     'VolumeType': 'gp2'
#                 },
#             },
#             {
#                 'DeviceName': '/dev/xvdb',
#                 'Ebs': {
#                     'Encrypted': False,
#                     'DeleteOnTermination': True,
#                     'VolumeSize': 500,
#                     'VolumeType': 'gp2'
#                 },
#             }
#         ],
#         ImageId='ami-2803ac4e',
#         InstanceType='m4.xlarge',
#         KeyName='bnbJumpServerRoot',
#         MaxCount=1,
#         MinCount=1,
#         Monitoring={'Enabled': True},
#         SecurityGroupIds=[office_group_id],
#         SubnetId=web_a,
#         DisableApiTermination=False,
#         EbsOptimized=True,
#         PrivateIpAddress='1.11',
#         TagSpecifications=[
#             {'ResourceType': 'volume','Tags': [{'Key': 'Name', 'Value': 'Web1'}]},
#             {'ResourceType': 'instance','Tags': [{'Key': 'Name', 'Value': 'Web1'}]}
#         ]
#     )
#
# except ClientError as e:
#     print(e)