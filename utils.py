import string


def remove_punctuation(text):
    # string.punctuation, Python'da içinde bulunan tüm noktalama işaretlerini içeren bir karakter dizisidir.
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def count_words(text):
    words = text.split()
    return len(words)


def calculate_speech_rate_wpm(original_duration, number_of_words):
    return (number_of_words / original_duration) * 60


def calculate_articulation_rate_wpm(speech_duration, number_of_words):
    return (number_of_words / speech_duration) * 60


def calculate_articulation_rate_spm(speech_duration, number_of_syllables):
    return (number_of_syllables / speech_duration) * 60


def calculate_speech_rate_spm(original_duration, number_of_syllables):
    return (number_of_syllables / original_duration) * 60


def count_syllables(text):
    return len(text) // 10


def get_audio_analysis(text: str, mysp: object, use_praat: bool, use_words: bool):
    text = remove_punctuation(text)

    speech_duration = mysp.speech_duration_analysis()
    original_duration = mysp.original_duration_analysis()
    number_of_pauses = mysp.pause_analysis()
    number_of_words = count_words(text)
    number_of_syllables = 198  # count_syllables(text) bunla ilgili başarılı bir repo var kullanılabilir.

    if use_praat:
        number_of_syllables = mysp.syllables_analysis()
        rate_of_speech = mysp.speech_rate_analysis()
        articulation_rate = mysp.articulation_rate_analysis()
    elif use_words:
        rate_of_speech = calculate_speech_rate_wpm(original_duration, number_of_words)
        articulation_rate = calculate_articulation_rate_wpm(speech_duration, number_of_words)
    else:
        rate_of_speech = calculate_speech_rate_spm(original_duration, number_of_syllables)
        articulation_rate = calculate_articulation_rate_spm(speech_duration, number_of_syllables)

    return speech_duration, original_duration, number_of_pauses, rate_of_speech, articulation_rate, number_of_syllables


# Dönen rate'lerin spm mi wpm mi olduğunun bilinmesi lazım !!!!!!!!!!
def calculate_speech_ratio(speech_duration, original_duration):
    return speech_duration / original_duration * 100


def result_audio_analysis(rate_of_speech, articulation_rate, speech_duration, original_duration, thresh=50):
    speech_ratio = calculate_speech_ratio(speech_duration, original_duration)

    if speech_ratio > thresh:
        if articulation_rate < 80:
            print("speech mode is too slow")
        elif 90 < articulation_rate < 110:
            print("speech mode is slow")
        elif 110 < articulation_rate < 160:
            print("speech mode is normal")
        elif 160 < articulation_rate < 180:
            print("speech mode is fast")
        elif 180 < articulation_rate:
            print("speech mode is too fast")
    else:
        if rate_of_speech < 70:
            print("speech mode is too slow")
        elif 70 < rate_of_speech < 100:
            print("speech mode is slow")
        elif 100 < rate_of_speech < 120:
            print("speech mode is normal")
        elif 120 < rate_of_speech < 150:
            print("speech mode is fast")
        elif 150 < rate_of_speech:
            print("speech mode is too fast")

# FileName, Gender, Mood, Speed, Lang, Pronounciation
# 0001.wav, Female, Read, 2x,     TR,    98,
# 0002.wav, Male,   Free, 1x,     EN,    89,
#
