import cv2
import os
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("training.yml")
names = []
for users in os.listdir("dataset"):
    names.append(users)
img = cv2.imread("test\ABHIMANYU.jpg")
while True:

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray_image[y : y + h, x : x + w])
        print(id)
        if id:
            cv2.putText(
                img,
                names[id - 1],
                (x, y - 4),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                1,
                cv2.LINE_AA,
            )
        else:
            cv2.putText(
                img,
                "Unknown",
                (x, y - 4),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                1,
                cv2.LINE_AA,
            )
    cv2.imshow("Recognize", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
