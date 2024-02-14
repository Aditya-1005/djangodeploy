from django.shortcuts import render
from django.shortcuts import HttpResponse
import boto3
import pandas as pd
import numpy as np
import os
from configparser import ConfigParser
from io import StringIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from botocore.exceptions import ClientError


def read_csv(filename,bucket):
    config = ConfigParser()
    # config.read('credentials.config')
    # aws_access_id = config.get('section','aws_access_id')
    # aws_secret_key = config.get('section','aws_secret_key')
    object_key = filename
    bucket_name=bucket
    # client = boto3.client('s3',aws_access_key_id=aws_access_id,aws_secret_access_key=aws_secret_key)
    client = boto3.client('s3')
    response = client.get_object(Bucket=bucket_name,Key=object_key)
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
    if status == 200:
        print(f"Successful S3 get_object response. Status - {status}")
        obj = response['Body']
        df= pd.read_csv(StringIO(obj.read().decode('utf-8')))
    else:
        print(f"Unsuccessful S3 get_object response. Status - {status}")
    df= df.dropna(axis=0,how='all')
    return df

@api_view(['GET'])
def home(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bucket = 'awsdemodjango'
    file_name = 'employee.csv'
    df = read_csv(filename=file_name,bucket=bucket)
    final = df.to_json(orient='records', lines=True)
    return Response(final, status=status.HTTP_200_OK)

def hello(request):
    return HttpResponse('Hello User. You can now consume this api!!!')