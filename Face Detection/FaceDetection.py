import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('kids.jpg')
resized_image = cv2.resize(image, (700, 400))

image_gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(image_gray, 1.1, 4)

for x, y, w, z in face:
    resized_image = cv2.rectangle(resized_image, (x, y), (x+w, y+z), (255, 0 ,0), 2)

cv2.imshow("Face Detection", resized_image)
cv2.waitKey(0)
input('')