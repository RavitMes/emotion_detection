"""
This module opens the webcam independently in a greyscale colors and uses the
Haar Cascade Object Detection Face to detect the face in the frame.
The detected face is marked real-time by a rectangle frame, and subsequently it captures 50 frames with
150msec delay between each frame while saving the original frames, cropping the face from the frame,
resize it to (48,48) and save it in an array of cropped_faces.

After capturing all frames the array shape is the following: (48,48,i<=50), and this array will be
given as an input for the model to predict the face expression.
Here i stands for the number of captured faces from the frames.
i can be less than 50 since we take into account that in some frames whether no face
was detected or more than one face were detected.
For convenience, some show functions were added to the code in order to show the face detection
and the functionality of the code.
"""

import cv2
import matplotlib.pyplot as plt
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# defining webcam as the video (0 represent the default option which is the web camera).
cap = cv2.VideoCapture(0)
cropped_faces = []
i=0

while i<50:
    # Read the frame
    _, img = cap.read()

    # take 50 frames with 150 msec delay between each frame
    for i in range(50):
        _, frame = cap.read()
        #convert the frame to gray scale
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #detect the faces in the picture using the classifier face_cascade
        faces_rects = face_cascade.detectMultiScale(gray_image, 1.1, 4)
        # print how many faces were found in the current frame
        print(f'frame{i} found: ', len(faces_rects))
        # writing the frames as a grey scale colored
        cv2.imwrite(f'camera_frame{i}.png', gray_image)
        #wait 150 msec
        cv2.waitKey(150)

        # check if no faces were detected / more than one face was dete
        if len(faces_rects) != 1:
            #(the following line will be changed by logger)
            #if the condition is fulfilled, instead of adding picture to the croped_faces list,
            # add the following string indicating the number of the frame not found
            cropped_faces.append(f"face in frame {i} not recognized/more than one face were found")
            print("face not fount")

        #otherwise
        else:
             # Draw the rectangle around each face
            for (x, y, w, h) in faces_rects:
                cv2.rectangle(gray_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # Display
                cv2.imshow('img', gray_image)
                #add the cropped face from the current gray image to a list of cropped faces
                cropped_faces.append(gray_image[y:y + h, x:x + w])
    #setting the i to 50 in order to exit the loop after capturing 50 frames
    i = 50
#releasing the camera
cap.release()

#resize all pictures to (48,48) and put them inside a list
resized_arr=[]
for face in cropped_faces:
    if type(face) is not str:
      resized_face = cv2.resize(src=face, dsize=(48,48), interpolation=cv2.INTER_CUBIC)
      #showing the resized picture
      plt.imshow(resized_face)
      resized_arr.append(resized_face)
      plt.show()
