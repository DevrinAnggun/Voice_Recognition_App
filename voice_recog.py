from abc import ABC, abstractmethod
import speech_recognition as sr

# Receiver
class MediaPlayer:
    def playSong(self):
        print("Memutar lagu favorit...")

    def pause(self):
        print("Video dijeda.")

    def nextTrack(self):
        print("Lagu berikutnya diputar.")

    def stop(self):
        print("Musik dihentikan.")

    def previousTrack(self):
        print("Kembali ke lagu sebelumnya.")

    def volumeUp(self):
        print("Volume dinaikkan.")

    def volumeDown(self):
        print("Volume diturunkan.")

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class PlaySongCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.playSong()

class PauseVideoCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.pause()

class NextTrackCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.nextTrack()

class StopMusicCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.stop()

class PreviousTrackCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.previousTrack()

class VolumeUpCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.volumeUp()

class VolumeDownCommand(Command):
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.volumeDown()

# Invoker
class VoiceController:
    def __init__(self):
        self.commands = {}

    def setCommand(self, commandName, command):
        self.commands[commandName.lower()] = command

    def executeCommand(self, commandName):
        command = self.commands.get(commandName.lower())
        if command:
            command.execute()
        else:
            print(f"Perintah '{commandName}' tidak dikenali.")

# Main program with speech recognition and exit feature
if __name__ == "__main__":
    player = MediaPlayer()
    controller = VoiceController()

    # Mendaftarkan command
    controller.setCommand("putar lagu favorit", PlaySongCommand(player))
    controller.setCommand("pause video", PauseVideoCommand(player))
    controller.setCommand("next track", NextTrackCommand(player))
    controller.setCommand("stop musik", StopMusicCommand(player))
    controller.setCommand("kembali ke lagu sebelumnya", PreviousTrackCommand(player))
    controller.setCommand("naikkan volume", VolumeUpCommand(player))
    controller.setCommand("turunkan volume", VolumeDownCommand(player))

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("=== Silakan ucapkan perintah suara ===")
    print("Ucapkan 'selesai' atau 'keluar' untuk menghentikan program.\n")

    while True:
        with mic as source:
            print("Mendengarkan...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command_text = recognizer.recognize_google(audio, language="id-ID")
            command_text_lower = command_text.lower()
            print(f"Perintah dikenali: {command_text}")

            if command_text_lower in ["selesai", "keluar"]:
                print("Program dihentikan. Terima kasih!")
                break

            controller.executeCommand(command_text)

        except sr.UnknownValueError:
            print("Maaf, suara tidak dapat dikenali.")
        except sr.RequestError as e:
            print(f"Error layanan pengenalan suara: {e}")

        print()
