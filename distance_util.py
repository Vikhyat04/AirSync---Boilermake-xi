camWidth = None
camHeight = None


def setCamSize(width, height):
    global camWidth, camHeight
    camWidth = width
    camHeight = height


def distanceBetweenLandmarks(a, b):
    return (((a.x - b.x) * camWidth) ** 2 + (
            (a.y - b.y) * camHeight) ** 2) ** 0.5


def xDistanceBetweenLandmarks(a, b):
    return (a.x - b.x) * camWidth


def yDistanceBetweenLandmarks(a, b):
    return (a.y - b.y) * camHeight
