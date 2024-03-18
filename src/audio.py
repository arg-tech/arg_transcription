import logging
import wave
from transformers import pipeline
from src.templates import BertTEOutput
#logging configuration
logging.basicConfig(datefmt='%H:%M:%S',
                    level=logging.DEBUG)

class AudioTranscriber:
    def __init__(self):
        self.generator = pipeline(model="facebook/wav2vec2-base-960h", return_timestamps="word")

    def create_xAIF(self, transcript):
        return BertTEOutput.format_output(transcript)  

    def audio_transcribe(self, audio_path):
        logging.info('file path...............: {}'.format(audio_path))
        transcripts = self.generator(audio_path)
        logging.info('the transcript...............: {}'.format(transcripts['text']))
        return self.create_xAIF(transcripts['text'])



