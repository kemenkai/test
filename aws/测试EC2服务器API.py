# -*- coding: UTF-8 -*-
import local_ami
import create_instances
import describe_instances
import modify_instance_attribute
import security_group
import subnet
import terminate_instances
import check_vpc
import time


# 0 : pending
# 16 : running
# 32 : shutting-down
# 48 : terminated
# 64 : stopping
# 80 : stopped

vpc_id = check_vpc.local_vpc()

security_id = subnet.check_Subnets(local_profile_name='default',local_vpc_id=vpc_id)
