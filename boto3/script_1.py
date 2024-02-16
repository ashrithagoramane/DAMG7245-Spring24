import boto3
import uuid

s3_resource = boto3.resource('s3')

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

BUCKET_NAME = create_bucket_name("damg7245demo")
print(f"Creating bucket {BUCKET_NAME}")
s3_resource.create_bucket(Bucket=BUCKET_NAME)

bucket_obj = s3_resource.Bucket(name=BUCKET_NAME)

print(f"Uploading a file to bucket {BUCKET_NAME}")
file_name = "sample.txt"
bucket_obj.upload_file(
    Filename=file_name, Key=file_name)
