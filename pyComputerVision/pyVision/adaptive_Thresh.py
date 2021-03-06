
"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Unlimited Capture --> 0
green_color = (0,255,0)
position = (100, -100)
font = cv2.FONT_HERSHEY_SIMPLEX



def click():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")


    #read image from file, turns it Black and white, gets dimenstions
    picture_1 = cv2.imread('Picture1.png', 0)
    height, width = picture_1.shape[0:2]

    #Creates names window, shows picture taken
    cv2.namedWindow("Picture")
    cv2.imshow("Picture", picture_1)
   
    #Thresh hold values, creates thresh hold image from one taken
    user_thresh_id = 125
    userChoice = str(user_thresh_id) 
    ret, user_thresh = cv2.threshold(picture_1, user_thresh_id, 255, cv2.THRESH_BINARY)

    #, out
    cv2.putText(user_thresh, userChoice, (300, 300), font, 4, (0,255,0), 4, cv2.LINE_AA)
    cv2.imshow("CV USER THRESH", user_thresh)

    thres_adapt = cv2.adaptiveThreshold(picture_1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow("Adaptive Threshold", thres_adapt)


cv2.namedWindow("Video")

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=1, fy=1)
    cv2.imshow("Video", frame)

    ch2 = cv2.waitKey(1)
    if ch2 & 0xFF == ord('p'):
        click()
    elif ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

