# Creating an EC2 instance again but this time using Python

import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId = 'ami-0f75cb5a4a1ca2993',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'studentT00164220',
    SubnetId = 'subnet-2972a665')
print (instance[0].id)
