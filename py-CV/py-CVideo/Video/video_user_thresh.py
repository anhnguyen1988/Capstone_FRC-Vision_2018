"""
In this code:

1. User defined threshold
2. Gass Blur
3. Contours
4. Contour filtering

End Output - This will find a 5' x 3' reflective tape square
    about 4 feet away from the camera


Press 'q' to quit


"""


import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Video Scource

cv2.namedWindow("Video")


while(True):

    #Pulls image from stream
    ret, takePic1 = cap.read()
    
    #Converts image from R,G,b to Gray Scale
    takePic1 = cv2.cvtColor(takePic1, cv2.COLOR_RGB2GRAY)

    #Bluring the image, for easier ID, Gaussian Blur
    takePic1 = cv2.GaussianBlur(takePic1, (3,3),0)

    #User Threshold 
    thresh = 160
    ret, user_thresh = cv2.threshold(takePic1, thresh, 255, cv2.THRESH_BINARY)

    #Finding contours, writing to object 'contours'
    _, contours, hierarchy = cv2.findContours(user_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print(len(contours))

    #Array for holding filtered contours
    filtered = []
    

    #For loop for filtering out contours based on pixel Area
    for c in contours:
        if cv2.contourArea(c) < 1000:
            continue
        elif cv2.contourArea(c) > 3000:
            continue
        else:
            filtered.append(c)
    print(len(filtered))

    objects = np.zeros([takePic1.shape[0], takePic1.shape[1],3], 'uint8')


    for c in filtered:
               
        #Draws and outline around the contour, green
        cv2.drawContours(objects, [c], -1, (0,255,0), 3)

        
        #Centriod
        # Had to add +1 to advoid Dividion by Zero erro
        M = cv2.moments(c)
        cx = int( M['m10']/(M['m00'] + 1))
        cy = int( M['m01']/(M['m00'] + 1))

        #Centriods
        cv2.circle(objects, (cx,cy), 4, (0, 0, 255), -1)
        #Area and Perimter
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)

        print("(X,Y): ", cx, cy, "Area: ", area, "Perimter: ", perimeter)
    
    cv2.imshow("Video", user_thresh)


    cv2.imshow("Objects", objects)


    #Picture / Break if statement
    ch2 = cv2.waitKey(1)
    if ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
