import pyttsx3

class Text2speech:
    engine: pyttsx3.engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[0].id)

    def text_to_speech(self,text: str, save: bool = False, file_name = 'out.mp3'):
        if save:
            self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()
