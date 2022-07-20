import boto3

s3 = boto3.client("s3")

with open('/Users/deepshah/Desktop/AWS_BOTO3/Rekognition/opencv_frame_0.png' , "rb") as f:
    data = f.read()


response = s3.put_object(
    ACL='public-read',
    Body=  data,
    Bucket='visionvirtualassistant',
    Key = "demoimage.png"
)
print(response)