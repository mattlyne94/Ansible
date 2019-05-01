import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    allocation = ec2.allocate_address(Domain='vpc-15434d7d')
    response = ec2.associate_address(AllocationId=allocation['eipalloc-0425716f21f53c60a'],
                                     InstanceId='i-0cc2c8c030f5ac905')
    print(response)
except ClientError as e:
    print(e)

