import boto3
from aws import check_vpc
from botocore.exceptions import ClientError

vpc_id = check_vpc.local_vpc()

def check_Subnets(args):
    session = boto3.Session(profile_name='kehu')
    client = session.client('ec2')
    response = client.describe_subnets(
        Filters=[
            {
                'Name':'vpc-id',
                'Values':[
                    vpc_id,
                ],
            }  ,
        ],
    )

    for num in range(len(response['Subnets'])):
        _prinvate_Subnets = response['Subnets'][num]
        Subnets_Zone =_prinvate_Subnets['AvailabilityZone']
        Subnets_Name = _prinvate_Subnets['Tags'][0]['Value']
        Subnets_Id = _prinvate_Subnets['SubnetId']
        Subnets_CidrBlock = _prinvate_Subnets['CidrBlock']
        # print(_prinvate_Subnets)
        print("Subnets_Name:{},Subnets_Id:{},Subnets_CidrBlock:{},Subnets_Zone:{}\n".format(Subnets_Name,Subnets_Id,Subnets_CidrBlock,Subnets_Zone))


# print(check_Subnets(vpc_id))
check_Subnets(vpc_id)