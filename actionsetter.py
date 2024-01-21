import keyboard

def getAction(oldAction):
    action = oldAction

    if keyboard.is_pressed('Space'):
        action = 'Volume'

    if keyboard.is_pressed('Enter'):
        action = 'Idle'

    return action
