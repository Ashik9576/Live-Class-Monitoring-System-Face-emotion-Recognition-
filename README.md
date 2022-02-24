# Live-Class-Monitoring-System-Face-emotion-Recognition-
# Introduction
Face Emotion recognition is the process of identifying human emotion. People vary widely in their accuracy at recognizing the emotions of others. Use of technology to help people with emotion recognition is a relatively nascent research area. Generally, the technology works best if it uses multiple modalities in context. To date, the most work has been conducted on automating the recognition of facial expressions from video, spoken expressions from audio, written expressions from text, and physiology as measured by wearables.

Facial expressions are a form of nonverbal communication. Various studies have been done for the classification of these facial expressions. There is strong evidence for the universal facial expressions of seven emotions which include: neutral happy, sadness, anger, disgust, fear, and surprise. So it is very important to detect these emotions on the face as it has wide applications in the field of Computer Vision and Artificial Intelligence. These fields are researching on the facial emotions to get the sentiments of the humans automatically.

![155081533-a356d549-087e-4387-9945-a2c67aa10dbf](https://user-images.githubusercontent.com/79791821/155364306-eb0e82fa-aa65-4c1b-b094-d42b0a67b863.png)

# Problem Statements
The Indian education landscape has been undergoing rapid changes for the past 10 years owing to the advancement of web-based learning services, specifically, eLearning platforms.

Global E-learning is estimated to witness an 8X over the next 5 years to reach USD 2B in 2021. India is expected to grow with a CAGR of 44% crossing the 10M users mark in 2021. Although the market is growing on a rapid scale, there are major challenges associated with digital learning when compared with brick and mortar classrooms. One of many challenges is how to ensure quality learning for students. Digital platforms might overpower physical classrooms in terms of content quality but when it comes to understanding whether students are able to grasp the content in a live class scenario is yet an open-end challenge. In a physical classroom during a lecturing teacher can see the faces and assess the emotion of the class and tune their lecture accordingly, whether he is going fast or slow. He can identify students who need special attention.

Digital classrooms are conducted via video telephony software program (ex-Zoom) where it’s not possible for medium scale class (25-50) to see all students and access the mood. Because of this drawback, students are not focusing on content due to lack of surveillance.

While digital platforms have limitations in terms of physical surveillance but it comes with the power of data and machines which can work for you. It provides data in the form of video, audio, and texts which can be analyzed using deep learning algorithms.

Deep learning backed system not only solves the surveillance issue, but it also removes the human bias from the system, and all information is no longer in the teacher’s brain rather translated in numbers that can be analyzed and tracked.

I will solve the above-mentioned challenge by applying deep learning algorithms to live video data. The solution to this problem is by recognizing facial emotions.

# What is Face Emotion Recognition?
* Facial emotion recognition is the process of detecting human emotions from facial expressions.
* The human brain recognizes emotions automatically, and software has now been developed that can recognize emotions as well.
* This is a few shot learning live face emotion detection system.
* The model should be able to real-time identify the emotions of students in a live class.

# Head-start References

❖ https://towardsdatascience.com/face-detection-recognition-and-emotion-detection-in-8-lines-of-code-b2ce32d4d5de

❖ https://towardsdatascience.com/video-facial-expression-detection-with-deep-learning-applying-fast-ai-d9dcfd5bcf10

❖ https://github.com/atulapra/Emotion-detection

❖ https://medium.com/analytics-vidhya/building-a-real-time-emotion-detector-towards-machine-with-e-q-c20b17f89220

# Dataset link
❖ https://www.kaggle.com/deadskull7/fer2013

# Dataset Information
The data comes from the past Kaggle competition “Challenges in Representation Learning: Facial Expression Recognition Challenge”. The faces have been automatically registered so that the face is more or less centered and occupies about the same amount of space in each image.

This dataset contains 35887 grayscale 48x48 pixel face images.

Each image corresponds to a facial expression in one of seven categories

Labels:

0 - Angry 😠

1 - Disgust 😧

2 - Fear 😨

3 - Happy 😃

4 - Sad 😞

5 - Surprise 😮

6 - Neutral 😐

# Project Approch
* Step 1. Build Model

We have used Five different models as follows:

Model 1- Mobilenet Model
Model 2- Dexpression Model
Model 3- CNN Model
Model 4- Densenet Model
Model 5- Resnet Mode 

* Step 2. Real Time Prediction

And then we perform Real Time Prediction on our best model using webcam on Google colab itself.

  - Run webcam on Google Colab
  - Load our best Model
  - Real Time prediction


* Step 3. Deployment

And lastly we have deployed it on Amazon WEB Services (AWS)

# Model Deployment:-
* Creating Web App Using Streamlit-
Streamlit is a Python framework for developing machine learning and data science web apps that is open-source. Using Streamlit, we can quickly create web apps and deploy them. You can use Streamlit to make an app the same way you'd make a Python programme. It's possible with Streamlit. Working on the interactive loop of coding and viewing results is a pleasure. In the web application.

* Deployment in cloud platform-
AWS (Amazon Web Services) is a comprehensive, evolving cloud computing platform provided by Amazon that includes a mixture of infrastructure as a service (IaaS), platform as a service (PaaS), and packaged software as a service (SaaS) offerings.

Deployment Link for AWS-

http://15.206.194.193:8501/

# Conclusion:
* All the models such as Mobilenet, Dexpression, CNN, Densenet, and ResNet were evaluated.
* The ResNet model was chosen because it had the highest training accuracy of all the models, and its validation accuracy was nearly 72 percent, which is comparable to CNN models.
* As a result, we save this resnet model and use it to predict facial expressions.
* Since, the emotion counts of disgust and surprise images are less therefore on local webcam it hardly detect those emotions.
* Using streamlit, a front-end model was successfully created and ran on a local webserver.The Streamlit web application has been deployed on Amazon's AWS cloud platform.
* It was an amazing and fascinating project. This has taught me a lot.
