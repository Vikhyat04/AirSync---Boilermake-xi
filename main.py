import multiprocessing as mp
from multiprocessing import Value, Array

import command_setter
import camera

from constants import commands

from extension_server import run_server

if __name__ == '__main__':
    command = Value('i', commands['Idle'])
    extensionClient = Array('c', b'')

    # speechRecognitionProcess = mp.Process(name='speechRecognitionProcess', target=command_setter.startSpeechRecognition, args=(command,))
    handDetectionProcess = mp.Process(name='handDetectionProcess', target=camera.startHandDetection, args=(command, extensionClient))

    # speechRecognitionProcess.start()
    handDetectionProcess.start()

    run_server(extensionClient)