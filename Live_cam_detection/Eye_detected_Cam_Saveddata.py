import cv2 as cv
# Load the cascade
face_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
# Read the input image
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Output.avi', fourcc,20.0,(640,480))
while True:
    _, img = cap.read()  #_, mean each frame from the video
# Convert into grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255 , 0 , 0), 2)
# Display the output
    out.write(img)
    cv.imshow("Press ESC key to terminate the Window",img)
    key = cv.waitKey(1)
    if key == 27:
        break 
cap.release()
out.release()
cv.destroyAllWindows()