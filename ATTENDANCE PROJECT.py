import cv2
import face_recognition
import numpy as np
import os
import csv
from datetime import datetime

path = ('ATTENDANCE IMAGES')
image = []
classname = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    image.append(curimg)
    classname.append(os.path.splitext(cl)[0])
    print(classname)

now = datetime.now()
current_date = now.strftime('%d-%m-%Y')
processed_names = set()

f = open(current_date + '.csv', 'a+', newline='')
writer = csv.writer(f)

def findencoding(imagess):
    encodelist = []
    for img in imagess:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        for encode in encodings:
            encodelist.append(encode)
    return encodelist

encodeknownlist = findencoding(image)
print('encoding completed')

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    sframes = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_sframe = cv2.cvtColor(sframes, cv2.COLOR_BGR2RGB)

    facescurframe = face_recognition.face_locations(sframes)
    encodecurframe = face_recognition.face_encodings(sframes, facescurframe)

    for encodefac, facloc in zip(encodecurframe, facescurframe):
        matches = face_recognition.compare_faces(encodeknownlist, encodefac)
        facdis = face_recognition.face_distance(encodeknownlist, encodefac)
        print(facdis)
        matchIndex = np.argmin(facdis)

        if matches[matchIndex]:
            name = classname[matchIndex].capitalize()
            if name not in processed_names:
                y1, x2, y2, x1 = facloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x2 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (220, 20, 60), 2)

                current_time = now.strftime('%H-%M-%S')
                writer.writerow([name, current_time])

                processed_names.add(name)

                for _ in range(60):
                    success, temp_frame = cap.read()
                    cv2.imshow('webcam', frame)
                    if cv2.waitKey(1) & 0xFF == 27:
                        break

    cv2.imshow('webcam', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        print("Exiting program...")
        break

cap.release()
cv2.destroyAllWindows()

f.close()
