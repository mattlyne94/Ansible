import boto3

s3 = boto3.client('s3')

s3.download_file('backup-bucket-13579', 'phpinfo.php', 'phpinfo.php')

