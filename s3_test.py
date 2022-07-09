import datetime
import boto3
from botocore.stub import Stubber, ANY
from s3 import S3

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
    """Use a context manager
    """
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

def test_sample3():
    """Use stub.ANY
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

    expected_params = {"Bucket": ANY}
    stubber.add_response("list_objects", response, expected_params)

    with stubber:
        service_response = s3.list_objects(Bucket="test-bucket")

    assert service_response == response

class StubS3(S3):
    def __init__(self):
        super().__init__()

        self.stubber = Stubber(self.client)

def test_StubS3():
    s3 = StubS3()

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
 
    expected_params = {"Bucket": ANY}
    s3.stubber.add_response("list_objects", response, expected_params)

    with s3.stubber:
        service_response = s3.list_objects(bucket="test-bucket")

    assert service_response == response

def test_S3():
    s3 = S3()

    stubber = Stubber(s3.client)

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
 
    expected_params = {"Bucket": ANY}
    stubber.add_response("list_objects", response, expected_params)

    with stubber:
        service_response = s3.list_objects(bucket="test-bucket")

    assert service_response == response
