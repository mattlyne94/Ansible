# Creating an EC2 instance again but this time using Python

import boto3
dryRun = False; # variable to put the script into dry run mode where the function allows it

ec2Client = boto3.client('ec2')
ec2Resource = boto3.resource('ec2')

# Create the instance
instanceDict = ec2Resource.create_instances(
    DryRun = dryRun,
    ImageId = 'ami-0f75cb5a4a1ca2993',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'studentT00164220',
    SubnetId = 'subnet-2972a665')

# Wait for the instance to launch before assigning Elastic IP
instanceDict[0].wait_until_running();

# Alllocate an Elastic IP
eip = ec2Client.allocate_address(DryRun=dryRun, Domain='vpc')

# Associate the elastic IP address with the instance launched above
ec2Client.associate_address(
    DryRun = dryRun,
    InstanceId = instanceDict[0].id,
    AllocationId = eip["AllocationId"])

