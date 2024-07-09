import json

import cv2

from src.analyzeFrame import analyzeFrame

with open("config.json") as file:
    config = json.load(file)

# define a video capture object
cap = cv2.VideoCapture(config["vidDevice"], cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CAP_PROP_FPS, 30)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

while (True):
    if not cap.isOpened():
        print("Error opening video stream")
        break

    # Capture the video frame by frame
    ret, frame = cap.read()

    # Display the resulting frame
    # cv2.imshow("frame", frame)
    cv2.imshow("frame", analyzeFrame(frame, config["tesseractPath"]))

    # the "q" button is set as the quitting button you may use any desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
