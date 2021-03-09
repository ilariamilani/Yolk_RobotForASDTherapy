import pyaudio
import wave
import time
import threading

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
THREESHOLD = 5


class PlayAudio:

    def __init__(self):
        self.wf = None
        self.stream = None

    def play(self, wav_file):
        self.wf = wave.open(wav_file, 'rb')
        p = pyaudio.PyAudio()
        self.stream = p.open(format=p.get_format_from_width(self.wf.getsampwidth()),
                             channels=self.wf.getnchannels(),
                             rate=self.wf.getframerate(),
                             output=True,
                             stream_callback=self.callback)
        self.stream.start_stream()
        while self.stream.is_active():
            time.sleep(0.1)
        # stop stream (6)
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()
        # close PyAudio (7)
        p.terminate()

    # define callback (2)
    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return data, pyaudio.paContinue
