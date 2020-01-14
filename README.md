Israel Tech Challenge Data Science Fellows Fall 20219 Final Project 
Olga, Moran, Ravit, Jake

 ### Real-Time Emotion Detection and Intervension
**The problem:** People are finding themselves in a downward spiral on the internet where they are doing things that hurt their mental health. There is no way of accurately assessing a users mental state in order to take steps to help them.

**Solution:** One of our ideas aims to recreate and improve on the accuracy and scope of emotion detection using a live feed instead of a single image like was done in previous projects. The idea would be to take a live feed from a user’s web camera and run an algorithm in the background that labels that users current mood in real time. Simultaneously, it will track the sentiment of the text in the webpage and if both the user is feeling a negative and the webpage sentiment is negative - it will alert the user using a popup.

**The Data:** Extended Cohn-Kanade Dataset - 327 image sequences and Ryerson Audio-Visual Database of Emotional Speech and Song if needed - 7356 video files

**Three Week Plan:** build a POC that can asses the user's emotion better than a random guess, and warn him from negative webpages.  

**Metric:** A simple accuracy metric could be used for the emotion detection since we have labeled data. However, if we want to detect depression for example, we may weight a false negative higher than a false positive. 

**Possible Problems** We may run into problems isolating faces in different environments. We may run into problems accessing the computer's webcamera. We may have problems getting the model working with a chrome extension.
 

**ideas to improve the project if we have enough time**:
1. add an algoritem that can recognize units of text. for examle, while browsing facebook, we will probably get better sentiment analysis accuracy if we send each post separately and not the whole page altogether.
2. in the initial version of the project the sentiment analysis will get the row frames from the webcam - in them, the user might be far away or in the sides of the webcame frame, which might lead to poor accuracy, since in the training set all faces are centered and in similar length of the camera. we can crop the user's face from the webcam frame and predict based on this in order to get better accuracy.

