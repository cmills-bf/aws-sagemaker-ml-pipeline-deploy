#!/usr/bin/python3

import boto3
from io import StringIO
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint")

client = boto3.client('sagemaker-runtime')

args = parser.parse_args()
endpoint = args.endpoint
endpoint_name = "breakfree-ml-pipeline-20230510202603" # Your endpoint name.
content_type = "text/csv"   # The MIME type of the input data in the request body.

payload = pd.DataFrame([[1.5,0.2,4.4,2.6]])
csv_file = StringIO()
payload.to_csv(csv_file, sep=",", header=False, index=False)
payload_as_csv = csv_file.getvalue()

response = client.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType=content_type,
    Body=payload_as_csv
    )

label = response['Body'].read().decode('utf-8')
print(label)