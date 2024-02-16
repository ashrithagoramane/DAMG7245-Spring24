import boto3
s3_resource = boto3.resource('s3')

BUCKET_NAME = "demo-bucket-damg7245-ashritha"

bucket_obj = s3_resource.Bucket(name=BUCKET_NAME)

print(f"Uploading a file to bucket {BUCKET_NAME}")
file_name = "sample.txt"
bucket_obj.upload_file(
    Filename=file_name, Key=file_name)
