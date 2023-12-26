import cv2

# Initialize the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is available
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Video Stream', frame)

    # Break the loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture when everything is done
cap.release()
cv2.destroyAllWindows()
