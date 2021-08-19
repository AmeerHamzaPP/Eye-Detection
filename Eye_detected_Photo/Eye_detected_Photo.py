import cv2 as cv
# Load the cascade
# face_cascade = cv.CascadeClassifier('haarcascade_face.xml')
face_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
# Read the input image
img = cv.imread('test.jpeg')
# Convert into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1 , 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv.imshow('img', img)
cv.imwrite("img.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()