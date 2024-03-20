import os

if __name__ == '__main__':
    print('Welcome to RoboSpeaker 1.1 created by Amalendu')
    while True:
        x = input('What you want me to speak: ')
        if x == "z":

            break
        command = f'echo {x} | powershell -command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())"'
        os.system(command)

