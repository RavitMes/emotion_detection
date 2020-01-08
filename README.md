Israel Tech Challenge Data Science Fellows Fall 20219 Final Project 
 
 ### Real-Time Emotion Detection and Intervension
**The problem:** People are finding themselves in a downward spiral on the internet where they are doing things that hurt their mental health. There is no way of accurately assessing a users mental state in order to take steps to help them.

**Solution:** One of our ideas aims to recreate and improve on the accuracy and scope of emotion detection using a live feed instead of a single image like was done in previous projects. The idea would be to take a live feed from a user’s web camera and run an algorithm in the background that labels that users current mood in real time. 

If we are able to achieve this goal easily, an extension of the idea would be to use this information somehow - one possibility would be to create a chrome extension that obfuscates certain words on the browser if the user’s sentiment is below a certain threshold. A further extension of this would be to try to keep a history of the effect of these changes to the user and optimize the obfuscation for maximum results. 

Another extension of the first goal could be to send an inspirational message or suggest a screen break.

The Test Metrics: A simple accuracy metric could be used for the emotion detection since we have labeled data. However, if we want to detect depression for example, we may weight a false negative higher than a false positive. 

**The Data:** Extended Cohn-Kanade Dataset 
 
 
 ### Generating Pictures of Flowers
**The problem:** creating new pictures of flowers, that can be adjusted based on specific characteristics (such as color and petal length) - for art and decoration perpuses - is time consuming and costly.

**Solution:** based on this video (watch seconds 5:50 - 6:20): https://www.youtube.com/watch?v=4VAkrUNLKSo&t=399s
the idea is to create a deep encoder that can characteristics of flowers from a latent feature space that is found using PCA and transform
them into an actual picture. changing the values of the latent space vector can control the characteristics of the flower. 

this project will have several stages:
 1. web scraping to enrich the flower pictures dataset.
 2. data preprocessing to make sure all pics have same shape and that flower is in the middle
 3. training the model
 4. building a simple GUI to help generating the flowers and changing its characteristics in a convenient way.

it can be extedened in the following ways:
1. using GANs to get more realistic results
2. using a more varialbe set of pictures (nature sceneries instead of flowers, for example)

**The Data:** https://www.kaggle.com/alxmamaev/flowers-recognition contains more than 4000 pictures of flowers. this dataset can be enriched by scraping google images

**metrics:** MSE between pixel values of original image and reconstructed image. also, we can see if the images the encoder outputs looks
realistic or not. 

**plan for three weeks** :we will build a POC, with low resolution and small number of pictures and encoder layers - just to show that the idea works. afterwards we can improve further on it.

**possible problems**: we might discover that the picture space is two big and will have to choose a diffrent kind of pictures with more
structure. 

