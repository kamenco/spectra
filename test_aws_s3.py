import boto3
import os

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

try:
    # Upload a test file
    s3.upload_file('test_file.txt', 'spectrakamen', 'test_file.txt')
    print("File uploaded successfully.")
except Exception as e:
    print("Error accessing S3:", e)

    import os

print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
print("AWS_SECRET_ACCESS_KEY:", os.getenv("AWS_SECRET_ACCESS_KEY"))
print("env.py loaded successfully")

