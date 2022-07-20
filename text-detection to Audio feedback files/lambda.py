import json

def lambda_handler(event, context):
    
    import codecs
    from boto3 import Session
    from boto3 import resource
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    s3 = resource('s3')
    bucket_name = "visionoutputdata"
    s3_object = s3.Bucket("visionoutputdata").Object("readme.txt").get()
    text = s3_object['Body'].read()
    print(text.decode())
    bucket = s3.Bucket(bucket_name)
    filename = "mynameis.mp3"
    myText = text.decode()

    response = polly.synthesize_speech(
    Text=myText,
    OutputFormat="mp3",
    VoiceId="Matthew")
    stream = response["AudioStream"]

    bucket.put_object(Key=filename, Body=stream.read())
