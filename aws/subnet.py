import boto3
import check_vpc
from botocore.exceptions import ClientError

# vpc_id2 = check_vpc.local_vpc()

def check_Subnets(local_profile_name=None,local_vpc_id=None,*args,**kwargs):
    __prinvate_vpc_id = local_vpc_id
    session = boto3.Session(profile_name=local_profile_name)
    client = session.client('ec2')
    response = client.describe_subnets(
        Filters=[
            {
                'Name' : 'vpc-id',
                'Values' : [
                    __prinvate_vpc_id
                ]
            }
        ]
    )

    Subnets_list = response['Subnets']

    for num in range(len(Subnets_list)):
        _prinvate_Subnets = Subnets_list[num]
        Subnets_Zone =_prinvate_Subnets['AvailabilityZone']
        Subnets_Name = _prinvate_Subnets['Tags'][0]['Value']
        Subnets_Id = _prinvate_Subnets['SubnetId']
        Subnets_CidrBlock = _prinvate_Subnets['CidrBlock']
        # print(_prinvate_Subnets)
        print("{} Subnets_Name:{}, Subnets_CidrBlock:{}, Subnets_Zone:{}, Subnets_Id:{}".format(num,Subnets_Name,Subnets_CidrBlock,Subnets_Zone,Subnets_Id))
        print("------------------------")

    subnets_id_num = []
    Subnets_id_list = []
    subnets_id_num = input("请选择需要的子网，多个子网使用 '|' 符号隔开：")
    if subnets_id_num.rfind('|') > 0:
        subnets_id_num = subnets_id_num.split('|')
        # print(subnets_id)
        print("您选择的子网为：")
        for num in range(len(subnets_id_num)):
            _local_subnets_id = int(subnets_id_num[num])
            _prinvate_Subnets = Subnets_list[_local_subnets_id]
            Subnets_Zone = _prinvate_Subnets['AvailabilityZone']
            Subnets_Name = _prinvate_Subnets['Tags'][0]['Value']
            Subnets_id_list.append(_prinvate_Subnets['SubnetId'])
            Subnets_CidrBlock = _prinvate_Subnets['CidrBlock']
            print("{} {}".format(Subnets_Name,Subnets_CidrBlock))
    else:
        _local_subnets_id = int(subnets_id_num)
        _prinvate_Subnets = Subnets_list[_local_subnets_id]
        Subnets_Zone = _prinvate_Subnets['AvailabilityZone']
        Subnets_Name = _prinvate_Subnets['Tags'][0]['Value']
        Subnets_id_list.append(_prinvate_Subnets['SubnetId'])
        Subnets_CidrBlock = _prinvate_Subnets['CidrBlock']
        print("您选择的子网为：")
        print("{} {}".format(Subnets_Name, Subnets_CidrBlock))

    return Subnets_id_list



# print(check_Subnets(vpc_id))
# check_Subnets(local_profile_name="kehu")




# zql_web_a = 'subnet-2ea32367'
# zql_web_c = 'subnet-3f6d9464'
# zql_rds_a = 'subnet-a8ac2ce1'
# zql_rds_c = 'subnet-0f6a9354'
# zql_alb_a = 'subnet-abae2ee2'
# zql_alb_c = 'subnet-836891d8'
# zql_mbx_a = 'subnet-50ab2b19'
# zql_mbx_c = 'subnet-066f965d'
# zql_block_a = 'subnet-1cad2d55'
# zql_network_inout = 'subnet-c7ae2e8e'
# zql_log_a = 'subnet-60a22929'
# zql_log_c = 'subnet-86c808dd'
# bnb_mbx_a = 'subnet-79fe3230'
# bnb_mbx_c = 'subnet-b93938e1'
# bnb_blcok_nat = 'subnet-5b53ff12'
# bnb_blcok_all = 'subnet-8523c4de'
# bnb_test = 'subnet-a4ea41ed'
# bnb_launchpad_a = 'subnet-2abc2c63'
# bnb_launchpad_c = 'subnet-397ab462'
# bnb_kr_vpn1 = 'subnet-04d40d6c'
# bnb_kr_vpn2 = 'subnet-7846b534'
# bnb_mkm_a = 'subnet-48c1a401'
# bnb_mkm_c = 'subnet-2a26f571'
# bnb_info_a = 'subnet-fb187db2'
# bnb_info_c = 'subnet-0d8a5956'
# bnb_es_server_a = 'subnet-bfb6fcf6'
# bnb_es_server_c = 'subnet-b49f19ef'
# dae_info_a = 'subnet-0c89f845'
# dae_info_c = 'subnet-8d64c8d6'