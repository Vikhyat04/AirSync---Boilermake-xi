import cv2

from hand_detector import HandDetector
from volume_control import getSpeakerOutputVolume, setVolume

from action_detector import detectAction

from distance_util import distanceBetweenLandmarks, setCamSize

from constants import commands, actions

from extension_server import send_message

import asyncio

def getCommand(command):
    try:
        command.acquire()
        value = command.value
        command.release()
    except:
        command.release()
        value = ""
    return value

async def startHandDetectionHelper(command, extensionClient):
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

    volume = 100

    commandVal = getCommand(command)
    action = None

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

        newAction = detectAction(landmarksQueue)

        if newAction != actions['Idle'] and newAction != action:
            await send_message(newAction, extensionClient)

        action = newAction

        newCommandVal = getCommand(command)

        if newCommandVal == commands['Volume'] and commandVal != commands['Volume']:
            volume = getSpeakerOutputVolume()

        commandVal = newCommandVal

        if commandVal == commands['Volume'] and len(landmarksQueue) > 1 and landmarksQueue[-1]:
            diff = distanceBetweenLandmarks(landmarksQueue[-1][0], landmarksQueue[-1][1]) - volume
            deltaVolume = diff / 5 * 2
            newVolume = round(volume + deltaVolume)
            setVolume(newVolume)

        cv2.imshow('img', image)
        cv2.waitKey(waitKey)


def startHandDetection(command, extensionClient):
    asyncio.run(startHandDetectionHelper(command, extensionClient))