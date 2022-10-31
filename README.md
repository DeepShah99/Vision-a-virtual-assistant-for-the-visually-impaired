# Vision
Proposed a Virtual Assistant as an Engineering Capstone Project, which aims to help visually impaired individuals in navigation.
Live feed captured from the Raspberry Pi is sent to Amazon Rekognition to extract information and insights.
Log Analysis is done on the feedback data with the help of AWS Athena to create stronger correlations in patterns and refine its navigation over time.
<br/><br/><br/><br/>
<img align="center" img width="774" alt="Screen Shot 2022-10-19 at 12 16 26 AM" src="https://user-images.githubusercontent.com/48095548/196517889-f02372ea-e621-439f-89af-68d8370186c0.png">

---

### Table of Contents


- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

The driving force behind this project is to work on a Virtual Assistant by leveraging the
power of cloud computing. The first and primary objective is to start with text detection
(It can be a billboard, a book’s cover letter, etc.). After successful detection, the feedback
on the detected text can be given by voice commands. The second phase will make this
assistant more advanced by installing Alexa on the pi. We want to create custom Alexa
skills to make our assistant more interactive. We could ask Alexa what the user saw at a
particular time and date... This can be achieved using S3 and Athena. As all the data will
be stored in S3 buckets, we could do a log analysis using simple SQL queries with the
help of AWS Athena.



#### Technologies

The AWS services we would like to leverage but are not limited to
- AWS Rekognition: To perform a visual analysis of the live video feed
- AWS Kinesis Video Streams: To transfer live video feed to AWS via Rasberry Pi
- AWS Lambda: To do serverless computing and interconnect all the services
- AWS S3: To store all the data
- AWS Alexa: To make the assistant more interactive
- AWS Polly: To perform the text-to-audio conversion

[Back To The Top](#Vision)

---

## How To Use

#### Installation

VisionScript.py has integrated all the services that are required for this project. 


[Back To The Top](#Vision)

---

## References
[Back To The Top](#Vision)

AWS documentation was always to the rescue. 

Lambda - https://aws.amazon.com/lambda/

Boto3 - https://aws.amazon.com/sdk-for-python/

S3 - https://aws.amazon.com/s3/

Rekognition - https://aws.amazon.com/rekognition/


---

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](# Vision: A Virtual Assistant for the Visually Impaired)

---

## Author Info

- Linkedin - [Jeevan Henry Dsouza](https://www.linkedin.com/in/jeevanhenrydsouza/)
- Website - [GitHub](https://github.com/JEEVANHENRYDSOUZA)

- Linkedin - [Deep Shah](https://www.linkedin.com/in/deep-shah-378458191/)
- Website - [GitHub](https://github.com/DeepShah99)


[Back To The Top](#Vision)
