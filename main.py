import multiprocessing as mp
from multiprocessing import Value

import command_setter
import camera

from constants import commands

if __name__ == '__main__':
    command = Value('i', commands['Idle'])

    speechRecognitionProcess = mp.Process(name='speechRecognitionProcess', target=command_setter.startSpeechRecognition, args=(command,))
    handDetectionProcess = mp.Process(name='handDetectionProcess', target=camera.startHandDetection, args=(command,))

    speechRecognitionProcess.start()
    handDetectionProcess.start()

    end = input()

    speechRecognitionProcess.terminate()
    handDetectionProcess.terminate()