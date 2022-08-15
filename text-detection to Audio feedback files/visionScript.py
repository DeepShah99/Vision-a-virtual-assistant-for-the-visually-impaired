import cv2
import os
import boto3
import json
from pprint import pprint
cam = cv2.VideoCapture(0)
 
cv2.namedWindow("test")
 
img_counter = 0
 
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
 
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite('/Users/deepshah/Desktop/AWS_BOTO3/Rekognition/{}'.format(img_name), frame)
        print("{} written!".format(img_name))
        img_counter += 1
 
cam.release()
 
cv2.destroyAllWindows() 

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

def detect_text(photo, bucket):


    count  = 1


    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    pprint(len(textDetections))
    #print ('Detected text\n----------')
   
    for text in textDetections:
        if count <= len(textDetections)//2:
            print ('Detected text:' + text['DetectedText'] + " " + str(text['Id']))
            with open('/Users/deepshah/Desktop/AWS_BOTO3/Rekognition/readme.txt', 'a') as f:
                f.write(text['DetectedText'] + " ")
        count+=1

    return len(textDetections)

def main():
    open('/Users/deepshah/Desktop/AWS_BOTO3/Rekognition/readme.txt', 'w').close()
    s3 = boto3.client("s3")
    
    for object in s3.list_objects(Bucket = "visionvirtualassistant")["Contents"]:
        print(object["Key"])
        bucket='visionvirtualassistant'
        photo= object["Key"]
        text_count=detect_text(photo,bucket)
        print("Text detected: " + str(text_count))
        print("\n\n")
    s3_upload = boto3.resource('s3')
    s3_upload.meta.client.upload_file('/Users/deepshah/Desktop/AWS_BOTO3/Rekognition/readme.txt', 'visionoutputdata', 'readme.txt')



   

if __name__ == "__main__":
    main()



lambda_client = boto3.client('lambda')


test_event = dict()

response = lambda_client.invoke(
    FunctionName='Lambda_Text_To_Speech',
    Payload = json.dumps(test_event)
)

print(response['Payload'])
print(response['Payload'].read().decode('utf-8'))

s3_resource = boto3.resource("s3")

s3_object = s3_resource.Object('visionoutputdata', 'mynameis.mp3')

s3_object.download_file('/Users/deepshah/Desktop/AWS_BOTO3/Rekognition/visionoutput.mp3')