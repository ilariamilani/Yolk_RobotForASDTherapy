import pyaudio
import audioop
import math
import time
#from timer import Timer
from clap import ClapAnalyzer

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 # Record at 44100 samples per second
CHUNK = 1024 * 2 # Number of samples in a chunk
# this is the threshold that determines whether or not sound is detected
THRESHOLD = 60 #45
LOW_THRESHOLD = 55 #35


class AudioActivity:

    def __init__(self):
        #self.t = Timer()
        self.clap_time = []
        self.sequence_identified = 0
        self.actual_sequence = None
        self.sequence = []
        self.noise = 0
        self.Nbeat = 0
        self.silence = 0
        self.elapsed_time = 0
        self.other_activity = 0
        self.p = None
        self.stream = None


    def initialize_sequences(self):
        self.sequence.append([1./4, 1./4, 1./2, 1./4, 1./4, 1./2])  # dindondan                           0
        self.sequence.append([1./8, 1./8, 1./4, 1./8, 1./8, 1./4])  # ticchetà                            1
        self.sequence.append([1./8, 1./8, 1./4, 1./8, 1./8, 1./4])  # opopop                              2
        self.sequence.append([1./4, 1./4, 1./4, 1./4, 1./4, 1./4, 1./2]) #twinkle twinkle                 3
        self.sequence.append([1./4, 1./4, 1./2, 1./8, 1./8, 1./4, 1./4]) #queen                           4
        self.sequence.append([1./8, 1./6, 1./8, 1./6, 1./8, 1./6, 1./4]) # brilla brilla stellina         5
        self.sequence.append([1./6, 1./6, 1./6, 1./6, 1./6, 1./6, 1./6, 1./6]) #giro giro tondo           6
        #self.sequence.append([1./4, 1./4, 1./4, 1./4, 1./4, 1./4, 1./4, 1./4]) #giro giro tondo
        self.sequence.append([1./4, 1./4, 1./4, 1./4, 1./4, 1./4, 1./2, 1./4, 1./4, 1./2]) #fra martino   7
        self.sequence.append([1./4, 1./4, 1./4, 1./4, 1./4, 1./4, 1./4]) #vecchia fattoria                8



        self.sequence.append([1./6, 1./6, 1./4, 1./6, 1./6, 1./6]) # ci vuole un fiore                    9
        self.sequence.append([1./4, 1./8, 1./8, 1./4, 1./4])  #tatititata                                 10
        # fra martino, bella lavanderina?


    def start(self, id):
        self.initialize_sequences()
        self.p = pyaudio.PyAudio()  # Create an interface to PortAudio

        # open your audio stream
        self.stream = self.p.open(format=FORMAT,
                        rate=RATE,
                        channels=CHANNELS,
                        input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback=self.audio_callback)
        self.choice_sequence(id)
        # start the stream
        self.stream.start_stream()

        # timer start
        #self.t.start()  # alla fine sottraggo il valore temporale del primo battito
        self.t1 = time.perf_counter()
        self.t2 = 0
        print("start timer")


    def choice_sequence(self, id):
        self.actual_sequence = ClapAnalyzer(
            self.sequence[id],
            deviation_threshold=0.2
        )
        self.actual_sequence.on_clap_sequence(self.on_sequence_detected)


    def on_sequence_detected(self):
        print("Sequence detected")
        self.sequence_identified = 1


    def add_clap(self, time):
        #    for clap_analyzer in sequence:
        #        clap_analyzer.clap(time)
        self.actual_sequence.clap(time)


    def audio_callback(self, in_data, frame_count, time_info, status):
        rms = audioop.rms(in_data, 2)  # quadratic mean of the data. width=2 for format=paInt16
        # print(rms)
        if rms == 0:
            decibel = 0
        else:
            decibel = 20 * math.log10(rms)  # transforms into db
        # check level against threshold
        #print(decibel)
        if decibel > THRESHOLD:
            self.noise += 1
            #elapsed_time = self.t.elapsed_time()
            self.t2 = time.perf_counter()
            self.elapsed_time = self.t2 - self.t1
            if self.Nbeat == 0:
                self.add_clap(self.elapsed_time)
                if self.sequence_identified > 0:
                    print("Found")
                self.clap_time.append(self.elapsed_time)
                print("performance started")
                print("clap")
                print(self.clap_time[self.Nbeat])
                self.Nbeat += 1
                self.silence = 0
            else:
                deltaT = self.elapsed_time - self.clap_time[self.Nbeat - 1]
                if (deltaT > 0.093) and (self.silence >= 1):
                    # test a 85 BPM devo avere un battito ogni 0.7 sec
                    print("clap")
                    self.clap_time.append(self.elapsed_time)
                    print(self.clap_time[self.Nbeat])
                    print(self.clap_time[:])
                    self.add_clap(self.elapsed_time)
                    if self.sequence_identified > 0:
                        print("Found")
                    self.Nbeat += 1
                    self.silence = 0
                if self.silence == 0 and self.noise >= 10:
                    self.other_activity += 1
                    print("other activity is detected")
        elif decibel < LOW_THRESHOLD:
            self.silence += 1
            self.noise = 0
            #if self.silence > 50:
                #print("silence")
        return in_data, pyaudio.paContinue

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        #self.sequence_identified = 0
        #self.clap_time = []
