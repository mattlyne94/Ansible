# import boto3 sdk
import boto3

# calling boto3 high-level resource
s3 = boto3.resource('s3')

# calling s3 create bucket function
# specifying unique bucket name
# specifying bucket geographical location
s3.create_bucket(Bucket='backup-bucket-13579', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})

