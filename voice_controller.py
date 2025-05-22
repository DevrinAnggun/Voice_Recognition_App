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
