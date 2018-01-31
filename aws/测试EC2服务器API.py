# -*- coding: UTF-8 -*-
from aws import ami
from aws import create_instances
from aws import describe_instances
from aws import modify_instance_attribute
from aws import security_group
from aws import subnet
from aws import terminate_instances
import time


# 0 : pending
# 16 : running
# 32 : shutting-down
# 48 : terminated
# 64 : stopping
# 80 : stopped

bnb_tokyo_vpc_id = 'vpc-08281e6c'
dae_tokyo_vpc_id = ''
# host = {'web1':{'HostName':'Web1','ip':'1.11','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
#         'web2':{'HostName':'Web2','ip':'2.11','GroupId':office_security_group_id,'SubnetId':web_c,'instancetype':'m4.xlarge'},
#         'admin_pnk':{'HostName':'AdminPnk','ip':'1.40','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
#         'admin_ex':{'HostName':'AdminEx','ip':'1.41','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
#         'stream1':{'HostName':'Stream1','ip':'1.50','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
#         'stream2':{'HostName':'Stream2','ip':'2.50','GroupId':office_security_group_id,'SubnetId':web_c,'instancetype':'m4.xlarge'},
#         'file':{'HostName':'File','ip':'1.49','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'m4.xlarge'},
#         'mongo':{'HostName':'Mongo','ip':'1.100','GroupId':office_security_group_id,'SubnetId':web_a,'instancetype':'c4.xlarge'},
#         'chat':{'HostName':'Chat','ip':'1.110','GroupId':public_security_group_id,'SubnetId':web_a,'instancetype':'c4.xlarge'},
#         'resource':{'HostName':'Resource','ip':'1.250','GroupId':public_security_group_id,'SubnetId':web_a,'instancetype':'c4.xlarge'},
#         'eng1':{'HostName':'MbxEng1','ip':'10.10','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.xlarge'},
#         'eng2':{'HostName':'MbxEng2','ip':'11.10','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.xlarge'},
#         'eng3':{'HostName':'MbxEng3','ip':'10.11','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.xlarge'},
#         'mgmt1':{'HostName':'MbxMgmt1','ip':'10.20','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'c4.2xlarge'},
#         'mgmt2':{'HostName':'MbxMgmt2','ip':'11.20','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'c4.2xlarge'},
#         'priv1':{'HostName':'MbxPriv1','ip':'10.30','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'priv2':{'HostName':'MbxPriv2','ip':'11.30','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'rest1':{'HostName':'MbxRest1','ip':'10.40','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'c4.2xlarge'},
#         'rest2':{'HostName':'MbxRest2','ip':'11.40','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'c4.2xlarge'},
#         'pub1':{'HostName':'MbxPub1','ip':'10.50','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'pub2':{'HostName':'MbxPub1','ip':'11.50','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'kline1':{'HostName':'MbxKline1','ip':'10.60','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'kline2':{'HostName':'MbxKline2','ip':'11.60','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'user1':{'HostName':'MbxUser1','ip':'10.70','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'agg1':{'HostName':'MbxAggTrade1','ip':'10.80','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'agg2':{'HostName':'MbxAggTrade2','ip':'11.80','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'rmqint1':{'HostName':'MbxRmqInt1','ip':'10.90','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'rmqint2':{'HostName':'MbxRmqInt2','ip':'11.90','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'rmqout1':{'HostName':'MbxRmqOut1','ip':'10.100','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'rmqout2':{'HostName':'MbxRmqOut2','ip':'11.100','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'rmqha1':{'HostName':'MbxRmqHa1','ip':'10.110','GroupId':private_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'rmqha2':{'HostName':'MbxRmqHa2','ip':'11.110','GroupId':private_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'http1':{'HostName':'MbxHttp1','ip':'10.120','GroupId':public_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.medium'},
#         'http2':{'HostName':'MbxHttp2','ip':'11.120','GroupId':public_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.medium'},
#         'wss1':{'HostName':'MbxWss1','ip':'10.130','GroupId':public_security_group_id,'SubnetId':mbx_a,'instancetype':'t2.large'},
#         'wss2':{'HostName':'MbxWss2','ip':'11.130','GroupId':public_security_group_id,'SubnetId':mbx_c,'instancetype':'t2.large'},
#         }

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
# create_instances(host['eng3']['HostName'],host['eng3']['ip'],host['eng3']['GroupId'],host['eng3']['SubnetId'],host['eng3']['instancetype'],disk_size=1025)
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
# create_instances('bnbMkm1','172.16.13.11',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm2','172.16.14.11',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm3','172.16.13.12',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm4','172.16.14.12',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm5','172.16.13.13',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm6','172.16.14.13',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm7','172.16.13.14',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm8','172.16.14.14',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm9','172.16.13.15',bnb_office_security_group_id,bnb_mkm_a,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbMkm10','172.16.14.15',bnb_office_security_group_id,bnb_mkm_c,'m4.xlarge',ami=mkm_ami,disk_size=2048,public_ip_status=True)
# create_instances('bnbZookeeper1','172.16.13.250',bnb_office_security_group_id,bnb_mkm_a,'t2.xlarge',ami=zookeeper_ami)

# info服务器购买
create_instances.create_instances('daeInfo1','172.16.13.10',security_group.dae_private_security_group_id,subnet.dae_info_a,'t2.xlarge',disk_size=200)


# 临时购买服务器
# create_instances('Test','172.16.0.100',bnb_office_security_group_id,bnb_test,'t2.2xlarge',ami=win_2016)
# create_instances('bnbWAVES','172.16.5.13',bnb_office_security_group_id,bnb_blcok_nat,'m4.xlarge',ami=ubuntu16_ami,disk_size=500)
# create_instances('zqlInnerhttp1','10.2.10.140',zql_private_security_group_id,zql_mbx_a,'t2.medium',disk_size=1024,profile_name="kehu")
# create_instances('zqlInnerhttp2','10.2.11.140',zql_private_security_group_id,zql_mbx_c,'t2.medium',disk_size=1024,profile_name="kehu")
# create_instances('daeInnerhttp1','10.1.10.140',dae_private_security_group_id,dae_mbx_a,'t2.medium',disk_size=1024,profile_name="kehu")
# create_instances.create_instances('daeInnerhttp2','10.1.11.140',security_group.dae_private_security_group_id,subnet.dae_mbx_a,'t2.medium',disk_size=1024,profile_name="kehu")

