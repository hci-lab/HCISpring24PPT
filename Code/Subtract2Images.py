import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is the default camera (webcam)

# Create a background subtractor object
# You can use either MOG2 or KNN
background_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
# background_subtractor = cv2.createBackgroundSubtractorKNN()
 
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Apply the background subtractor to get the foreground mask
    foreground_mask = background_subtractor.apply(frame)

    # Optional: Apply morphological operations to clean up the mask
  #  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
   # foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_OPEN, kernel)
    #foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_CLOSE, kernel)

    # Apply the mask to the original frame to extract the foreground
    #foreground = cv2.bitwise_and(frame, frame, mask=foreground_mask)

    # Display the original frame, foreground mask, and foreground
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Foreground Mask', foreground_mask)
    #cv2.imshow('Foreground', foreground)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()