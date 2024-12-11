import cv2
import os
import time



webcam = cv2.VideoCapture(0)
end_time = time.time() + 5
while time.time() < end_time:
    ret, frame = webcam.read()
    if ret:
        cv2.imshow('Camera Preview', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
num_images_to_capture =1
currentframe = 0


while currentframe < num_images_to_capture:
    success, frame = webcam.read()

    if not success:
        continue

    cv2.imshow('Webcam Feed', frame)

    username = input("Enter user name : ")

    image_path = os.path.join('ATTENDANCE IMAGES', f'{username}.jpg')
    cv2.imwrite(image_path, frame)
    currentframe += 1

    cv2.waitKey(1)

webcam.release()
cv2.destroyAllWindows()
