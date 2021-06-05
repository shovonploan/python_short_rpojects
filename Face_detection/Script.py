import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('C:/Users/Admin/Google Drive/Programming/Python_Prac/Projects/Face_detection/Tom-Holland-Face-PNG-Photos.png')
grayscalled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscalled_img)

# print(face_coordinates)

cv2.imshow('Demo Pic',grayscalled_img)
cv2.waitKey()