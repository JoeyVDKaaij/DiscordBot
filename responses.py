import random
import inputs

activity = True

def get_response(message: str) -> str:
    p_message = message.lower()
    p_messages = p_message.split()
    randomizer = random.randint(1,1000)

    if activity == True:
        if GetActivity(p_message) != '':
            return GetActivity(p_message)

    if p_message == 'hello' or p_message == 'hi':
        return 'Hey there!'

    elif p_message == 'roll':
        return str(random.randint(1,6))

    elif p_message == 'i\'m glad you like it!':
        return 'At least they can help YOU!'

    elif p_message == 'fuck you':
        return 'FUCK YOU'

    elif p_message == 'can you work?':
        random_int = random.randint(1, 3)
        if random_int == 1:
            return 'Nah'
        elif random_int == 2:
            return 'Could your mom work?'
        elif random_int == 3:
            return 'I don\'t feel like it!'

    elif p_message == 'any last words, bot?':
        return 'I hate my life'

    elif p_message == 'meow':
        return 'MEOW'

    elif p_message == 'nuh uh':
        if random.randint(0,1) == 0:
            return 'FYM NUH UH????'
        else:
            return 'YUH UH!'

    # elif p_message == 'skedaddle':
    #     return 'You\'ve shot Joey\'s laptop! Congratulations!! \n https://tenor.com/view/bsod-gif-26376970'

    elif p_message == 'good morning':
        return 'Good morning!'

    for messages in p_messages:
        if messages == 'cuh':
            return 'ON GOD'

        elif messages == 'potato':
            return ':potato:'

        elif messages == '🥔':
            return ':potato:'

        elif messages == 'eepy':
            return 'mimimimimi'

        elif messages == 'hihi':
            return 'HIHI'

        elif messages == 'fym':
            return 'FUCKED YOUR MOM'

        elif messages == 'yippee':
            return 'https://tenor.com/view/yippee-happy-celebration-joy-confetti-gif-25557730'

        elif messages == 'yo':
            return 'yo'

        elif randomizer == 1000:
            return 'YUM!'

        elif randomizer == 500:
            return 'https://tenor.com/view/purpgifs-fnaf-security-breach-fnaf-fnaf-memes-vanny-gif-24205928'

    return ''

def GetActivity(message: str) -> str:
    if message == 'left door':
        inputs.pressAndHoldKey('a', 0.1)

    elif message == 'right door':
        inputs.pressAndHoldKey('d', 0.1)

    elif message == 'middle vent':
        inputs.pressAndHoldKey('w', 0.1)

    elif message == 'right vent':
        inputs.pressAndHoldKey('f', 0.1)

    elif message == 'camera':
        inputs.pressAndHoldKey('s', 0.1)

    elif message == 'flashlight':
        inputs.pressAndHoldKey('z', 3)

    elif message == 'all off':
        inputs.pressAndHoldKey('x', 0.1)

    elif message == 'catch that fish':
        inputs.pressAndHoldKey('c', 0.1)

    elif message == 'fuck them ads':
        inputs.pressAndHoldKey('enter', 0.1)

    elif message == 'i have fans':
        inputs.pressAndHoldKey('spacebar', 0.1)

    elif message == 'fuck this':
        inputs.pressAndHoldKey('escape', 0.1)

    elif message == 'power generator':
        inputs.pressAndHoldKey('1', 0.1)

    elif message == 'silent ventilation':
        inputs.pressAndHoldKey('2', 0.1)

    elif message == 'heater':
        inputs.pressAndHoldKey('3', 0.1)

    elif message == 'power ac':
        inputs.pressAndHoldKey('4', 0.1)

    elif message == 'global music box':
        inputs.pressAndHoldKey('5', 0.1)

    elif message == 'mouse down':
        inputs.moveMouse(0, 1000)

    elif message == 'mouse up':
        inputs.moveMouse(0, -1000)

    elif message == 'mouse left':
        inputs.moveMouse(-1000, 0)

    elif message == 'mouse right':
        inputs.moveMouse(1000, 0)

    return ''