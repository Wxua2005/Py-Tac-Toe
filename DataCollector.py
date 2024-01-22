import cv2
import mediapipe as mp
import csv
from joblib import dump , load
import numpy as np

# 1 for thumbs up and 0 for palm 3 for thumbs_down
# df = thumbs_up
# df2 = palm
# df3 = thumbs_down

model = load('model.joblib')
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
lst = []
real_fieldnames = []
fieldnames = [(str(i) + "_x" , str(i) + "_y") for i in range(1,21)]
for i in fieldnames:
    for j in i:
        real_fieldnames.append(j)

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image2 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        for id , lm in enumerate(hand_landmarks.landmark):
            h , w , c = image.shape
            cx , cy = int(lm.x*w) , int(lm.y*h)
            print(id , cx , cy)
            if len(lst) < 40:
                lst.append(cx)
                lst.append(cy)
            if len(lst) == 40:
                lst.append(cx)
                lst.append(cy)
                with open("test.csv", mode="a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(lst)
                    lst = []

    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
