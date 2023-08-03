from myspsolution import MyPraatAnalysis
from utils import result_audio_analysis, get_audio_analysis

audio_path = "Sercan_TR_1.wav"
praat_path = "myspsolution.praat"

mysp = MyPraatAnalysis(sound_path=audio_path,
                       praat_path=praat_path)


transcript = """Geliştirilen projelerin teknik tasarım, kod geliştirme ve test aşamalarında yer almak, Yeni teknolojileri takip etmek, şirkete adapte edilmesinde görev almak, İş süreçlerinin geliştirilmesi ve sürdürülebilir kalabilmesi için gerekli çalışmaları yürütmek, Yazılım kalite standartlarının sağlanması ve iyileştirilmesi amacıyla ekip üyeleriyle birlikte faaliyetler yürütmek, Mevcut geliştirilen kodun bakımını gerçekleştirmek. Yazılım Geliştirme  departmanlarında yaz dönemi zorunlu staj görevini yerine getirecek yazılım mühendisi stajyeri."""

speech_duration, original_duration, number_of_pauses, rate_of_speech, articulation_rate = get_audio_analysis(transcript,
                                                                                                             mysp,
                                                                                                             use_praat=False)

result_audio_analysis(transcript, mysp)
