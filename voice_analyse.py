from logging_ops import GeneralLogger
from pydub import AudioSegment
from myspsolution import MyPraatAnalysis
from utils import result_audio_analysis
import json
import os


class VoiceAnalyzer:
    def __init__(self):
        self.logger = GeneralLogger().logger
        self.logger.info("Voice Analyzer is ready for analysis.")
        self.praat_path = "myspsolution.praat"

    def analyze(self, uuid):
        self.logger.info(f"Analyzer starts for uuid : {uuid}.")
        wav_path = self.get_wav_file(uuid)
        transcript = self.get_transcript(uuid)
        mysp = MyPraatAnalysis(sound_path=wav_path,
                               praat_path=self.praat_path)
        result = result_audio_analysis(uuid, transcript, mysp)
        self.logger.info(f"Voice Result is {result}.")
        self.logger.info(f"Analysis is completed for uuid : {uuid}.")
        return {
            "status": True,
            "result": result
        }

    def get_transcript(self, uuid):
        transcript_path = f"../Volume/{uuid}/transcript.json"
        if os.path.exists(transcript_path):
            with open(transcript_path, 'r', encoding="utf-8") as f:
                return json.load(f)["Transcript"]

    def get_wav_file(self, uuid):
        mp3_path = f"../Volume/{uuid}/audio.mp3"
        wav_path = f"../Volume/{uuid}/audio.wav"

        # convert wav to mp3
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        return wav_path
