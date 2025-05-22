import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, controller):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.controller = controller
        self.exit_commands = {"selesai", "keluar"}

    def start_listening(self):
        print("=== Silakan ucapkan perintah suara ===")
        print("Ucapkan 'selesai' atau 'keluar' untuk menghentikan program.\n")

        while True:
            with self.mic as source:
                print("Mendengarkan...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            try:
                command_text = self.recognizer.recognize_google(audio, language="id-ID")
                command_text_lower = command_text.lower()
                print(f"Perintah dikenali: {command_text}")

                if command_text_lower in self.exit_commands:
                    print("Program dihentikan. Terima kasih!")
                    break

                self.controller.executeCommand(command_text)

            except sr.UnknownValueError:
                print("Maaf, suara tidak dapat dikenali.")
            except sr.RequestError as e:
                print(f"Error layanan pengenalan suara: {e}")

            print()
