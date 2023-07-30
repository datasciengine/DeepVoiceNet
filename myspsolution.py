from scipy.stats import ks_2samp, binom, ttest_ind
from parselmouth.praat import call, run_file
import pandas as pd
import numpy as np


class MyPraatAnalysis:
    def __init__(self, sound_path: str, praat_path: str):
        self.objects = self.get_objects(sound_path, praat_path)
        self.z1 = str(self.objects[1])

    def get_objects(self, sound_path: str, praat_path: str):
        wdir = ""
        try:
            return run_file("asdadasdasda")
        except Exception as e:
            print(f"We couldnt get object item, process failed. Error could be {e}")

    def analyze(self):

        print(self.objects)

        # self.total_analysis()
        # print("_" * 30)
        # self.gender_mode_analysis()
        # print("_" * 30)
        # self.syllables_analysis()
        # print("_" * 30)
        # self.pause_analysis()
        # print("_" * 30)
        # self.speech_rate_analysis()
        # print("_" * 30)
        # self.articulation_rate_analysis()
        # print("_" * 30)
        # self.speech_duration_analysis()
        # print("_" * 30)
        # self.original_duration_analysis()
        # print("_" * 30)
        # self.balance_analysis()
        # print("_" * 30)
        # self.freq_0_mean_analysis()
        # print("_" * 30)
        # self.freq_0_stdev_analysis()
        # print("_" * 30)
        # self.freq_0_median_analysis()
        # print("_" * 30)
        # self.freq_0_min_analysis()
        # print("_" * 30)
        # self.freq_0_max_analysis()
        # print("_" * 30)
        # self.freq_0_q25_analysis()
        # print("_" * 30)
        # self.freq_0_q75_analysis()
        # print("_" * 30)
        # self.pronunciation_analysis()
        # print("_" * 30)

    def total_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = np.array(z2)
            z4 = np.array(z3)[np.newaxis]
            z5 = z4.T
            dataset = pd.DataFrame(
                {"number_ of_syllables": z5[0, :], "number_of_pauses": z5[1, :], "rate_of_speech": z5[2, :],
                 "articulation_rate": z5[3, :], "speaking_duration": z5[4, :],
                 "original_duration": z5[5, :], "balance": z5[6, :], "f0_mean": z5[7, :], "f0_std": z5[8, :],
                 "f0_median": z5[9, :], "f0_min": z5[10, :], "f0_max": z5[11, :],
                 "f0_quantile25": z5[12, :], "f0_quan75": z5[13, :]})
            print(dataset.T)
        except Exception as e:
            print("Try again the sound of the audio was not clear", e)
        return;

    def syllables_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[0])  # will be the integer number 10
            z4 = float(z2[3])  # will be the floating point number 8.3
            print("number_ of_syllables=", z3)
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def pause_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[1])  # will be the integer number 10
            z4 = float(z2[3])  # will be the floating point number 8.3
            print("number_of_pauses=", z3)
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def speech_rate_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[2])  # will be the integer number 10
            z4 = float(z2[3])  # will be the floating point number 8.3
            print("rate_of_speech=", z3, "# syllables/sec original duration")
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def articulation_rate_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[3])  # will be the floating point number 8.3
            print("articulation_rate=", z3, "# syllables/sec speaking duration")
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def speech_duration_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[4])  # will be the floating point number 8.3
            print("speaking_duration=", z4, "# sec only speaking duration without pauses")
        except:
            z4 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def original_duration_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[5])  # will be the floating point number 8.3
            print("original_duration=", z4, "# sec total speaking duration with pauses")
        except:
            z4 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def balance_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[6])  # will be the floating point number 8.3
            print("balance=", z4, "# ratio (speaking duration)/(original duration)")
        except:
            z4 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_mean_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[7])  # will be the floating point number 8.3
            print("f0_mean=", z4, "# Hz global mean of fundamental frequency distribution")
        except:
            z4 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_stdev_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[8])  # will be the floating point number 8.3
            print("f0_SD=", z4, "# Hz global standard deviation of fundamental frequency distribution")
        except:
            z4 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_median_analysis(self):

        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[3])  # will be the integer number 10
            z4 = float(z2[9])  # will be the floating point number 8.3
            print("f0_MD=", z4, "# Hz global median of fundamental frequency distribution")
        except:
            z4 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_min_analysis(self):

        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[10])  # will be the integer number 10
            z4 = float(z2[10])  # will be the floating point number 8.3
            print("f0_min=", z3, "# Hz global minimum of fundamental frequency distribution")
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_max_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[11])  # will be the integer number 10
            z4 = float(z2[11])  # will be the floating point number 8.3
            print("f0_max=", z3, "# Hz global maximum of fundamental frequency distribution")
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_q25_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[12])  # will be the integer number 10
            z4 = float(z2[11])  # will be the floating point number 8.3
            print("f0_quan25=", z3, "# Hz global 25th quantile of fundamental frequency distribution")
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def freq_0_q75_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[13])  # will be the integer number 10
            z4 = float(z2[11])  # will be the floating point number 8.3
            print("f0_quan75=", z3, "# Hz global 75th quantile of fundamental frequency distribution")
        except:
            z3 = 0
            print("Try again the sound of the audio was not clear")
        return;

    def pronunciation_analysis(self):
        try:
            z2 = self.z1.strip().split()
            z3 = int(z2[13])  # will be the integer number 10
            z4 = float(z2[14])  # will be the floating point number 8.3
            db = binom.rvs(n=10, p=z4, size=10000)
            a = np.array(db)
            b = np.mean(a) * 100 / 10
            print("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (b))
        except:
            print("Try again the sound of the audio was not clear")
        return;

    def gender_mode_analysis(self):
        try:
            # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
            z2 = self.z1.strip().split()
            z3 = float(z2[8])  # will be the integer number 10
            z4 = float(z2[7])  # will be the floating point number 8.3
            if z4 <= 114:
                g = 101
                j = 3.4
            elif z4 > 114 and z4 <= 135:
                g = 128
                j = 4.35
            elif z4 > 135 and z4 <= 163:
                g = 142
                j = 4.85
            elif z4 > 163 and z4 <= 197:
                g = 182
                j = 2.7
            elif z4 > 197 and z4 <= 226:
                g = 213
                j = 4.5
            elif z4 > 226:
                g = 239
                j = 5.3
            else:
                print("Voice not recognized")
                exit()

            def teset(a, b, c, d):
                d1 = np.random.wald(a, 1, 1000)
                d2 = np.random.wald(b, 1, 1000)
                d3 = ks_2samp(d1, d2)
                c1 = np.random.normal(a, c, 1000)
                c2 = np.random.normal(b, d, 1000)
                c3 = ttest_ind(c1, c2)
                y = ([d3[0], d3[1], abs(c3[0]), c3[1]])
                return y

            nn = 0
            mm = teset(g, j, z4, z3)
            while (mm[3] > 0.05 and mm[0] > 0.04 or nn < 5):
                mm = teset(g, j, z4, z3)
                nn = nn + 1
            nnn = nn
            if mm[3] <= 0.09:
                mmm = mm[3]
            else:
                mmm = 0.35
            if z4 > 97 and z4 <= 114:
                print("a Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
            elif z4 > 114 and z4 <= 135:
                print("a Male, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
            elif z4 > 135 and z4 <= 163:
                print("a Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
            elif z4 > 163 and z4 <= 197:
                print("a female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
            elif z4 > 197 and z4 <= 226:
                print("a female, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
            elif z4 > 226 and z4 <= 245:
                print("a female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
            else:
                print("Voice not recognized")
        except:
            print("Try again the sound of the audio was not clear")
