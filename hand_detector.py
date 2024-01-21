import cv2
import mediapipe as mp

connections = [(4, 8)]


class HandDetector(object):
    def __init__(self, mode=True, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mpHands = mp.solutions.hands.Hands(mode, maxHands, modelComplexity, detectionCon, trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def drawAndGetLandmarks(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.mpHands.process(imgRGB)
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, landmarks, connections,
                                           self.mpDraw.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                           self.mpDraw.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
        return img, results.multi_hand_landmarks
