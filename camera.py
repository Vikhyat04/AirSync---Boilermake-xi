import cv2

from handdetector import HandDetector
from volumecontrol import getSpeakerOutputVolume, setVolume

from actionsetter import getAction
from commanddetector import detectCommand

from distanceutil import distanceBetweenLandmarks, setCamSize

camWidth = 800
camHeight = 500
setCamSize(camWidth, camHeight)

cameraIndex = 1
waitKey = 10
detector = HandDetector()

queueMaxSize = 100
landmarksQueue = []

capture = cv2.VideoCapture(cameraIndex)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, camWidth)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, camHeight)

action = 'Idle'

volume = 100

while True:
    success, image = capture.read()
    image, landmarks = detector.drawAndGetLandmarks(image)

    if len(landmarksQueue) >= queueMaxSize:
        landmarksQueue.pop(0)

    try:
        landmarks = landmarks[0].landmark
        landmarksQueue.append((landmarks[4], landmarks[8]))
    except:
        landmarksQueue.append(None)

    print(detectCommand(landmarksQueue))

    newAction = getAction(action)

    if newAction == 'Volume' and action != 'Volume':
        volume = getSpeakerOutputVolume()

    action = newAction

    if action == 'Volume' and len(landmarksQueue) > 1 and landmarksQueue[-1]:
        diff = distanceBetweenLandmarks(landmarksQueue[-1][0], landmarksQueue[-1][1]) - volume
        deltaVolume = diff / 5 * 2
        newVolume = round(volume + deltaVolume)
        setVolume(newVolume)

    cv2.imshow('img', image)
    cv2.waitKey(waitKey)
