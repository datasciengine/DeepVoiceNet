import string
import json


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


def calculate_speech_ratio(speech_duration, original_duration):
    return speech_duration / original_duration * 100


def get_audio_analysis(text: str, mysp: object, use_praat: bool):
    text = remove_punctuation(text)

    speech_duration = mysp.speech_duration_analysis()
    original_duration = mysp.original_duration_analysis()
    balance = mysp.balance_analysis()
    number_of_pauses = mysp.pause_analysis()
    number_of_words = count_words(text)

    if use_praat:
        rate_of_speech = mysp.speech_rate_analysis()
        articulation_rate = mysp.articulation_rate_analysis()
    else:
        rate_of_speech = calculate_speech_rate_wpm(original_duration, number_of_words)
        articulation_rate = calculate_articulation_rate_wpm(speech_duration, number_of_words)

    return speech_duration, original_duration, number_of_pauses, rate_of_speech, articulation_rate


def detect_audio_speed(rate_of_speech, articulation_rate, speech_duration, original_duration, thresh=50):
    speech_ratio = calculate_speech_ratio(speech_duration, original_duration)

    if speech_ratio > thresh:
        if articulation_rate < 80:
            speech_speed = "too slow"
        elif 90 < articulation_rate < 110:
            speech_speed = "slow"
        elif 110 < articulation_rate < 160:
            speech_speed = "normal"
        elif 160 < articulation_rate < 180:
            speech_speed = "fast"
        elif 180 < articulation_rate:
            speech_speed = "too fast"
    else:
        if rate_of_speech < 70:
            speech_speed = "too slow"
        elif 70 < rate_of_speech < 100:
            speech_speed = "slow"
        elif 100 < rate_of_speech < 120:
            speech_speed = "normal"
        elif 120 < rate_of_speech < 150:
            speech_speed = "fast"
        elif 150 < rate_of_speech:
            speech_speed = "too fast"
    return speech_speed


def result_audio_analysis(uuid, text, mysp):
    speech_duration, original_duration, number_of_pauses, rate_of_speech, articulation_rate = get_audio_analysis(text,
                                                                                                                 mysp,
                                                                                                                 use_praat=False)
    speech_speed = detect_audio_speed(rate_of_speech, articulation_rate, speech_duration, original_duration, thresh=50)
    data = {
        "OriginalDuration": original_duration,
        "SpeechDuration": speech_duration,
        "NumOfPauses": number_of_pauses,
        "SpeechRate": round(rate_of_speech, 1),
        "ArticulationRate": round(articulation_rate, 1),
        "SpeechSpeed": speech_speed
    }
    voice_json_path = f"../Volume/{uuid}/voice.json"

    with open(voice_json_path, 'w') as file:
        json.dump(data, file)

    return data
