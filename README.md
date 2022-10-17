# Twitter-Sentiment-Analysis
A sentiment analysis tool deployed on AWS which analyzes the behavior of tweets giving and opinion on people's reaction on the matter.



## Abstract

Since humans express their thoughts and feelings more openly than ever before, sentiment analysis is fast becoming an essential tool to monitor and understand sentiment in all types of data.

Automatically analyzing customer feedback, such as opinions in survey responses and social media conversations, allows brands to learn what makes customers happy or frustrated, so that they can tailor products and services to meet their customers’ needs.

For example, using sentiment analysis to automatically analyze 4,000+ open-ended responses in your customer satisfaction surveys could help you discover why customers are happy or unhappy at each stage of the customer journey.

Maybe you want to track brand sentiment so you can detect disgruntled customers immediately and respond as soon as possible. Maybe you want to compare sentiment from one quarter to the next to see if you need to take action. Then you could dig deeper into your qualitative data to see why sentiment is falling or rising.

The overall benefits of sentiment analysis include:
- Sorting Data at Scale
- Real-Time Analysis
- Consistent criteria

To understand the goal and challenges of sentiment analysis, here are some examples:
- Netflix has the best selection of films
- Hulu has a great UI
- I dislike like the new crime series
- I hate waiting for the next series to come out



## Introduction

Tweets are often useful in generating a vast amount of sentiment data upon analysis. These data are useful in understanding the opinion of the people about a variety of topics.

Sentiment analysis is used in social media monitoring, allowing businesses to gain insights about how customers feel about certain topics, and detect urgent issues in real time before they spiral out of control. Brands of all shapes and sizes have meaningful interactions with customers, leads, even their competition, all across social media. By monitoring these conversations you can understand customer sentiment in real time and over time, so you can detect disgruntled customers immediately and respond as soon as possible.

Hence I have developed and deployed a very basic module of Sentiment Analysis on tweets on twitter to estimate a population's reaction towards a particular tweet


## Technologies and Services Used

#### AWS EC2

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment.

I have used the Django framework to develop frontend of my web app and used AWS EC2 to host our website.

![image](https://user-images.githubusercontent.com/61236166/195972134-9e5cf0c8-c3b4-4db0-a122-82c165c4aa3f.png)

#### AWS API Gateway

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.


![image](https://user-images.githubusercontent.com/61236166/195972347-effc7589-4b64-4de1-a9c5-652a35d73e8c.png)


#### AWS Lambda

AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. I have used AWS Lambda to run our code without any external servers.


<img src="https://user-images.githubusercontent.com/61236166/195972368-0bdf8e7b-44a1-46e4-9e73-d23d25faa002.png" width="500"/> <img src="https://user-images.githubusercontent.com/61236166/195972443-0ce16f94-395d-4b41-a83f-8598e04da0a1.png" width="500"/>


#### AWS Relational Database (RDS)

Amazon Relational Database Service (RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. I have used AWS Relational Databases (RDS) to store the user’s information.


![image](https://user-images.githubusercontent.com/61236166/195972528-bc05326d-5b17-41a0-99ff-4bde3ef08d8e.png)


#### AWS SES (Simple Email Service)

Amazon Simple Email Service (SES) is a cost-effective, flexible, and scalable email service that enables developers to send mail from within any application. I have used AWS SES (Simple Email Service) to send an email to users for notifications when they register. When any user registers for this service, a verification email is sent to his specified email and upon verification, the user can use it to send emails.




<img src="https://user-images.githubusercontent.com/61236166/195972602-937af4e9-a74e-4137-8d90-24fd6c624e54.png" width="500"/> <img src="https://user-images.githubusercontent.com/61236166/195972604-bd03f107-9a2c-426b-bc5d-373ccb56d314.png" width="500"/>



<img src="https://user-images.githubusercontent.com/61236166/195972606-c7ae132f-cbab-48aa-904e-8ff0b59ef921.png" width="500"/> <img src="https://user-images.githubusercontent.com/61236166/195972607-98355d1a-7297-4ab4-abe2-6241970d3108.png" width="500"/>



#### AWS Comprehend

Amazon Comprehend is a natural-language processing (NLP) service that uses machine learning to uncover valuable insights and connections in text. I
have used this service in order to assess the sentiments of the tweets and provide meaningful insights.


![image](https://user-images.githubusercontent.com/61236166/195972745-62f7b6bf-1af0-4ef1-a09b-b63a872ff0e5.png)


#### AWS Cloudwatch

It helps in monitoring our application, analyzing and optimizing resource utilization.


#### MySQL WorkBench

MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. MySQL Workbench provides data modeling, SQL development, and comprehensive administration tools for server configuration, user administration, backup, and much more. MySQL Workbench is available on Windows, Linux and Mac OS X.
I have used this to store registered user's database in order to access the webapp.

![image](https://user-images.githubusercontent.com/61236166/195973128-390bd77f-84c9-4d77-87b8-c231a9d7ddce.png)


#### Python and it's framework Django


## Some screenshots of the webapp

#### Login Page

![image](https://user-images.githubusercontent.com/61236166/195973148-4c7fcd08-bf7e-4e41-bef7-afe35faf326f.png)


#### Home Page

![image](https://user-images.githubusercontent.com/61236166/195973171-9df3b544-4184-4dad-b673-9ffc9d475e92.png)


#### Sentiment Analysis Result

![image](https://user-images.githubusercontent.com/61236166/195973181-62fc359e-90c9-43a9-b618-f22ed2a30bb9.png)


## How To Run This Project

I don't want to get your anxious but there are a lot of steps involved in order to successfully implement and run this project. First of all, you will need an AWS account. Then you will also need to download MySQL Workbench. Once you have both of these, please follow the below steps:
- Please type AWS EC2 in the search console and create a new instance and an elastic IP in order to host your website. (Assuming you already know how to create an instance and link it. If not, please refer to the link : https://aws.amazon.com/pm/ec2/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&s_kwcid=AL!4422!3!467723097967!p!!g!!amazon%20ec2&ef_id=CjwKCAjwtKmaBhBMEiwAyINuwLUp3DM0PBZRgiFvc4LxmQCcB8fAvJG-iTTwOnn2UxMW3JUxp8ckJhoCLwcQAvD_BwE:G:s&s_kwcid=AL!4422!3!467723097967!p!!g!!amazon%20ec2
- Now you will need to go to AWS API Gateway and create an API in order for your backend to connect to front end. If you don't know how to do the same, please refer to : https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html
- Now we will need to create a database in order to store the user's login information.
- For this we use AWS RDS. Go to RDS and create a database. You can also refer to: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html
- Next, you will need to setup AWS SES. Please follow the link : https://docs.aws.amazon.com/ses/latest/dg/setting-up.html
- Once done, please create an AWS S3 bucket to get access to and store your database. Please refer to : https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html
- On your AWS console, search for AWS Lambda and click on it.
- Once you are in AWS Lambda, on the left panel, click on functions and Create a function called Comprehend.
- After that, you will see an option called Add Trigger, click on that and add API Gateway from the list.
- Once created, please click on the Add Trigger option and select add API Gateway.
- Scroll below, you will see an option called code, click on that and at the top right corner, there will be an option called import from. Click on that and select add .zip. Here please  add the file lambda_function.py from the repository given above.
- Once created, please click on Add Trigger and add API Gateway again and link the API that you have created earlier.
- Then scroll below, and in the code section you will see an option to upload from. Click on that and select the zip file option.
- Here you will upload the entire package named "twitterSentimentalAnalysis-af7cb393-29ec-4d4a-a967-b300af915fde" given above in my repository.
- Here, we can test if all the steps performed till now are going well or not. For this, you can click on the test option and configure input values to the database. If the invocation function works and if the json formal is saved in the database, then you are good to go. Otherwise please go through the documentation again and check the connections.
- Once the test works, you can copy the IP in your EC2 and run the web app and ta-da, you have a webapp to analyze the sentiments of any tweet. You will just need to signup and you must receive the verification email in the email ID that you have linked to the SES. Then in the homepage, just paste the link of any tweet link and you should be good to go.
#### - Note: You will also need an access to twitter API for which you will need a developer's account. Please visit the link : https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api



## It's a medium level project with expertise required in AWS, SQL, Python Django. Hence, I hope the above documentation helps. Do contact me if you have any questions or doubts or feedback.
