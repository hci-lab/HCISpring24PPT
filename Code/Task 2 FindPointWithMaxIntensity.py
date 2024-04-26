import numpy as np
import cv2


cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture('ParkinsonianGait.mp4')
framecnt=0

while cap.isOpened():
    # read frame from capture object
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        #break
    frame = cv2.resize(frame, (640,480))
    orig = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    
    cv2.circle(gray, maxLoc, 5, (255, 0, 0), 2)
    # display the results of the naive attempt
    cv2.imshow("Gray Scale", gray)
    cv2.circle(frame, maxLoc, 5, (255, 0, 0), 2)
    # display the results of the naive attempt
    cv2.imshow("Color", frame)
    if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()