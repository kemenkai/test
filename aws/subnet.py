import boto3
import check_vpc
from botocore.exceptions import ClientError

# vpc_id2 = check_vpc.local_vpc()

def check_Subnets(local_profile_name='default',local_vpc_id=None,*args,**kwargs):
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
