import cv2
import mediapipe as mp


stack = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    succes,img = stack.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = Hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handler in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handler,mpHands.HAND_CONNECTIONS)

    cv2.imshow("Gambar",img)
    cv2.waitKey(1)