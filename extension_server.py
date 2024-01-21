import websockets

import cv2

from hand_detector import HandDetector
from volume_control import getSpeakerOutputVolume, setVolume

from action_detector import detectAction

from distance_util import distanceBetweenLandmarks, setCamSize

from constants import commands, actions

import asyncio

activeCommand = None

def getCommand():
    try:
        activeCommand.acquire()
        value = activeCommand.value
        activeCommand.release()
    except:
        activeCommand.release()
        value = ""
    return value

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

async def send_message(message, client):
    await client.send(message)

async def new_client_connected(client_socket, path):
    print("New client connected!")
    await startHandDetection(client_socket)

async def startHandDetection(client_socket):
    volume = 100

    commandVal = getCommand()
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
            await send_message(str(newAction), client_socket)

        action = newAction

        newCommandVal = getCommand()

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

async def start_server():
    print("Starting server...")
    await websockets.serve(new_client_connected, "localhost", 12345)

def run_server(command):
    global activeCommand
    activeCommand = command
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()