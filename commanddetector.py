from distanceutil import xDistanceBetweenLandmarks, yDistanceBetweenLandmarks

commandFrameCount = 5
registerDistance = 200

def detectCommand(landmarksQueue):
    if len(landmarksQueue) < commandFrameCount:
        return 'No Hand'

    if not landmarksQueue[-commandFrameCount] or not landmarksQueue[-1]:
        return 'Idle'

    if xDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) >= registerDistance:
        return 'Left Swipe'
    if xDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) <= -registerDistance:
        return 'Right Swipe'
    if yDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) >= registerDistance:
        return 'Up Swipe'
    if yDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) <= -registerDistance:
        return 'Down Swipe'

    return 'No Matches'