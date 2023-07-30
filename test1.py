from myspsolution import MyPraatAnalysis

audio_path = "normal_okuma-0.5.wav"
praat_path = "myspsolution.praat"

mysp = MyPraatAnalysis(sound_path=audio_path,
                       praat_path=praat_path)

mysp.analyze()
