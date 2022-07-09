import boto3
import botocore
from typing import Dict

class S3():
    def __init__(self):
        self.client = boto3.client("s3")

    def list_object(self, bucket: str) -> Dict:
        try:
            return self.client.list_objects(Bucket=bucket)
        except botocore.exceptions.ClientError as e:
            print(e)
            return
        except Exception as e:
            print(f"Other reason: {e}")

if __name__ == "__main__":
    s3 = S3()
    s3.list_object("hoge")
