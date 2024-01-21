import subprocess
import re


def getSpeakerOutputVolume():
    cmd = "osascript -e 'get volume settings'"
    process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.stdout.strip().decode('ascii')
    pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
                         r"alert volume:(\d+), output muted:(true|false)")
    volume, _, _, muted = pattern.match(output).groups()
    volume = int(volume)
    muted = (muted == 'true')
    return 0 if muted else volume


def setVolume(newVolume):
    if newVolume < 0:
        newVolume = 0
    if newVolume > 100:
        newVolume = 100

    subprocess.run(f"osascript -e 'set volume output volume {newVolume}'", stdout=subprocess.PIPE, shell=True)
