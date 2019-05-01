import boto3

s3 = boto3.client('s3')

filename = '/var/www/html/phpinfo.php'
bucket_name = 'backup-bucket-13579'

# Uploads file using a managed uploader, which can split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)

