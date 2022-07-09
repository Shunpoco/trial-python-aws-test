import datetime
import boto3
from botocore.stub import Stubber

def test_sample():
    """This sample is from https://botocore.amazonaws.com/v1/documentation/api/latest/reference/stubber.html
    """
    s3 = boto3.client("s3")
    stubber = Stubber(s3)

    response = {
        "IsTruncated": False,
        "Name": "test-bucket",
        "MaxKeys": 1000,
        "Prefix": "",
        "Contents": [{
            "Key": "test.txt",
            "ETag": '"abc123"',
            "StorageClass": "STANDARD",
            "LastModified": datetime.datetime(2016, 1, 20, 22, 9),
            "Owner": {"ID": "abc123", "DisplayName": "myname"},
            "Size": 14814,
        }],
        "EncodingType": "url",
        "ResponseMetadata": {
            "RequestId": "abc123",
            "HTTPStatusCode": 200,
            "HostId": "abc123",
        },
        "Marker": ""
    }

    expected_params = {"Bucket": "test-bucket"}
    stubber.add_response("list_objects", response, expected_params)
    stubber.activate()

    service_response = s3.list_objects(Bucket="test-bucket")
    assert service_response == response

def test_sample2():
    s3 = boto3.client("s3")
    
    response = {
        "Owner": {
            "ID": "foo",
            "DisplayName": "bar",
        },
        "Buckets": [{
            "CreationDate": datetime.datetime(2016, 1, 20, 22, 9),
            "Name": "baz",
        }],
    }

    with Stubber(s3) as stubber:
        stubber.add_response("list_buckets", response, {})
        service_response = s3.list_buckets()

    assert service_response == response
