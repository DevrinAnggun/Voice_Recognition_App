from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

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
