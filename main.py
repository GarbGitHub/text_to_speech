import pyttsx3


class Speak:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'ru')

    def __init__(self, text=None, rate=None, volume=None, voice_speaker=None):
        self.text = text
        self.rate = rate
        self.volume = volume
        self.voice_speaker = voice_speaker
        self._text_to_speech()

    def _text_to_speech(self):
        # voices: Artemiy, Yuriy, Evgeniy-Rus, Irina

        for voice in Speak.voices:
            if voice.name == self.voice_speaker:
                self.engine.setProperty('voice', voice.id)

        if self.rate:
            speed = self.rate
            self.rate = Speak.engine.getProperty('rate')
            self.engine.setProperty('rate', self.rate + speed)

        if self.volume:
            volume = self.volume
            self.volume = Speak.engine.getProperty('volume')
            self.engine.setProperty('volume', self.volume + volume)

        if self.text:
            Speak.engine.say(text=self.text)

        else:
            Speak.engine.say(text='Не расслышал, повторите!')

        Speak.engine.runAndWait()
        Speak.engine.stop()

Speak(
    text='Путин рассказал о главных нерешенных проблемах в стране',
    rate=40,
    volume=-0.50,
    voice_speaker='Irina'  # Artemiy, Yuriy, Evgeniy-Rus, Irina
)
