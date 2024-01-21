from distance_util import xDistanceBetweenLandmarks, yDistanceBetweenLandmarks

commandFrameCount = 5
registerDistance = 200


def detectAction(landmarksQueue):
    if len(landmarksQueue) < commandFrameCount:
        return 'Not enough frames'

    if not landmarksQueue[-commandFrameCount] or not landmarksQueue[-1]:
        return 'No Hand'

    if xDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) >= registerDistance:
        return 'Left Swipe'
    if xDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) <= -registerDistance:
        return 'Right Swipe'
    if yDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) >= registerDistance:
        return 'Up Swipe'
    if yDistanceBetweenLandmarks(landmarksQueue[-1][1], landmarksQueue[-commandFrameCount][1]) <= -registerDistance:
        return 'Down Swipe'

    return 'No Matches'
