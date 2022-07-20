
import boto3

def detect_text(photo, bucket):


    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    #print ('Detected text\n----------')
   
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            with open('Rekognition/readme.txt', 'a') as f:
                f.write(text['DetectedText'] + " ")
    return len(textDetections)

def main():
    open('Rekognition/readme.txt', 'w').close()
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
