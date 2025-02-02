import keyboard
import time
import mouse

keypressed = []

def pressAndHoldKey(key=f'', timelength=1):
    keyboard.press(f'{key}')
    keypressed.append(f'{key}')
    time.sleep(timelength)
    keyboard.release(f'{key}')
    keypressed.remove(f'{key}')

def pressKeyAfterKey(key1, key2, timeLength):
    keyboard.press(f'{key1}')
    keypressed.append(f'{key1}')
    time.sleep(timeLength)
    keyboard.press(f'{key2}')
    keypressed.append(f'{key2}')
    time.sleep(timeLength)
    keyboard.release(f'{key1}')
    keypressed.remove(f'{key1}')
    keyboard.release(f'{key2}')
    keypressed.remove(f'{key2}')

def clickMouse(button, timeLength):
    mouse.click(button)
    time.sleep(timeLength)
    mouse.release(button)

def moveMouse(addedPositionX, addedPositionY):
    mouse.move(addedPositionX, addedPositionY, absolute=False)

def moveMouseAbsolute(addedPositionX, addedPositionY):
    mouse.move(addedPositionX, addedPositionY)


def stopAllInputs():
    for keypress in keypressed:
        keyboard.release(keypress)