import time

import cv2
# import HyperFAS
from HyperFAS.src import demo
import numpy as np


def __main__(video_path):
    cap = cv2.VideoCapture(video_path)
    # reading video frames and loading them into an array (since video is short)
    col_images = []
    while cap.isOpened():
        ret, frame = cap.read()
        if (ret):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = (cv2.resize(frame, (224, 224)) - 127.5) / 127.5
            col_images.append(frame)
        else:
            break
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    t = time.time()  # recording time for assessing performance
    scores = demo.test_one(col_images)  # getting results for each frame by passing the array
    print("prediction time = {}".format(time.time() - t))
    return "Probability of video being spoofed: {}".format(np.mean(scores))
