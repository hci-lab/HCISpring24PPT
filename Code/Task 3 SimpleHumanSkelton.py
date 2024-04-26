import os
import cv2
import mediapipe as mp
# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=.5,
    min_tracking_confidence=0.5)

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
    #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    
    framecnt+=1
    # convert the frame to RGB format
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print (framecnt)
    # process the RGB frame to get the result
    results = pose.process(RGB)
        # Loop through the detected poses to visualize.
    
    
   
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    # show the final output
    cv2.imshow('Output', frame)

    if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()