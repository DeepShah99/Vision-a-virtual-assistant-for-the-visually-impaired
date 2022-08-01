import json
import boto3

lambda_client = boto3.client('lambda')


test_event = dict()

response = lambda_client.invoke(
    FunctionName='Lambda_Text_To_Speech',
    Payload = json.dumps(test_event)
)

print(response['Payload'])
print(response['Payload'].read().decode('utf-8'))