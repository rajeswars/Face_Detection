import cv2
import logging

logging.basicConfig(level=logging.INFO)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    logging.error("Could not open webcam")
    exit()

user_name = input("Enter user name and press <return> --> ")

if not user_name:
    logging.error("Name cannot be empty")
    exit()

logging.info(f"Initializing face detection for {user_name}")

while True:
    ret, frame = cam.read()

    if not ret:
        logging.error("Failed to read frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(30, 30))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        cv2.putText(frame, "Face Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, "No Face Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()