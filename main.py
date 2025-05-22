from media_player import MediaPlayer
from commands import (
    PlaySongCommand, NextTrackCommand,
    StopMusicCommand, PreviousTrackCommand, VolumeUpCommand, VolumeDownCommand
)
from voice_controller import VoiceController
from speech_recognizer import SpeechRecognizer

if __name__ == "__main__":
    player = MediaPlayer()
    controller = VoiceController()

    # Register commands tanpa pause video
    controller.setCommand("putar lagu favorit", PlaySongCommand(player))
    controller.setCommand("next track", NextTrackCommand(player))
    controller.setCommand("stop musik", StopMusicCommand(player))
    controller.setCommand("kembali ke lagu sebelumnya", PreviousTrackCommand(player))
    controller.setCommand("naikkan volume", VolumeUpCommand(player))
    controller.setCommand("turunkan volume", VolumeDownCommand(player))

    recognizer = SpeechRecognizer(controller)
    recognizer.start_listening()
