import boto3
from botocore.exceptions import ClientError
import sys

vpc_dict = {"daeVPC":"vpc-806975e4","zqlVPC":"vpc-d055b9b7","bnbVPC":"vpc-08281e6c"}

def local_vpc():
    _private_list = []
    vpc_num = 0

    for k in vpc_dict.keys():
        print("{} {}:{}".format(vpc_num,k,vpc_dict[k]))
        _private_list.append(k)
        vpc_num=vpc_num + 1

    vpc = int(input("请根据序号选择您需要的Vpc: "))
    vpc_name = _private_list[vpc]
    vpc_id = vpc_dict[vpc_name]
    print("您选择的Vpc是: \n序号：{}\nVPC名称：{}\nvpcID：{}\n".format(vpc,vpc_name,vpc_id))
    return vpc_id