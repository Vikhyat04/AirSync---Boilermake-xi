from distance_util import xDistanceBetweenLandmarks, yDistanceBetweenLandmarks

from constants import actions

commandFrameCount = 5
registerDistance = 200

def detectAction(landmarksQueue):
    if len(landmarksQueue) < commandFrameCount:
        return actions['Idle']

    if not landmarksQueue[-commandFrameCount] or not landmarksQueue[-1]:
        return actions['Idle']

    if xDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) >= registerDistance:
        return actions['Left Swipe']
    if xDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) <= -registerDistance:
        return actions['Right Swipe']
    if yDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) >= registerDistance:
        return actions['Up Swipe']
    if yDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) <= -registerDistance:
        return actions['Down Swipe']

    return actions['Idle']
