import multiprocessing as mp
from multiprocessing import Value
import command_setter
from constants import commands
from extension_server import run_server

if __name__ == '__main__':
    command = Value('i', commands['Idle'])

    # speechRecognitionProcess = mp.Process(name='speechRecognitionProcess', target=command_setter.startSpeechRecognition, args=(command,))
    # speechRecognitionProcess.start()

    run_server(command)