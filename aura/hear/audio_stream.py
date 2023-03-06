import threading
import uuid
from pathlib import Path

import pyaudio

# TODO: create a path when installing aura, for configs and records
import os
cwd = os.getcwd()

from aura.file_manager import AudioWriter

class AudioRecorder(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop_event = threading.Event()
        self.event_uuid = uuid.uuid4()
        self.root_path = Path(cwd) / "aura_records"

        # TODO: make this configurable
        self.audio_config = {'output_channels': 2, 
                            'framerate': 44100,
                            'format': pyaudio.paInt16,
                            'frames_per_buffer': 1024,
                            'mic_input_index': 0,
                            'audio_output_index': 2,
                            }

    def run(self):
        # open the microphone and audio output streams
        p = pyaudio.PyAudio()
        mic_stream = self._create_mic_stream(p)
        output_stream = self.__create_output_stream(p)

        # create a mixer object
        mixer = self._create_audio_mixer(p)

        # record and mix the audio
        mixed_frames = self._record_and_mix([mic_stream, output_stream], mixer)

        # save the mixed audio to a file with AudioWriter
        writer = AudioWriter(self.root_path)
        writer.write(self.event_name,
                     mixed_frames,
                     framerate=self.audio_config['framerate'],
                     channels=self.audio_config['output_channels'],
                     )

        # terminating the pyaudio instance
        p.terminate()

    def stop(self):
        self.stop_event.set()

    def _create_mic_stream(self, pyaudio_instance):
        return pyaudio_instance.open(self.audio_config['format'], 
                                     channels=1, 
                                     rate=self.audio_config['framerate'], 
                                     input=True, 
                                     frames_per_buffer=self.audio_config['frames_per_buffer'],
                                     input_device_index=self.audio_config['mic_input_index']
                                     )

    def _create_output_stream(self, pyaudio_instance, input_device_index):
        return pyaudio_instance.open(self.audio_config['format'], 
                                     channels=2, 
                                     rate=self.audio_config['framerate'], 
                                     input=True, 
                                     frames_per_buffer=self.audio_config['frames_per_buffer'],
                                     input_device_index=input_device_index
                                     )

    def _create_audio_mixer(self, pyaudio_instance):
        return pyaudio_instance.open(self.audio_config['format'], 
                                     channels=2, 
                                     rate=self.audio_config['framerate'], 
                                     output=True)

    def _record_and_mix(self, audio_streams, mixer) -> list:
        # record audio streams until the stop event is set
        frames = []
        while not self.stop_event.is_set():
            # TODO: find a way to do this for a variable number of audio streams
            mic_data = audio_streams[0].read(self.audio_config['frames_per_buffer'])
            output_data = audio_streams[1].read(self.audio_config['frames_per_buffer'])
            mixed_data = (mic_data + output_data) // len(audio_streams)
            mixer.write(mixed_data)
            frames.append(mixed_data)
        
        # if the stop event is set, close the audio streams and the mixer
        for stream in audio_streams:
            stream.stop_stream()
            stream.close()

        mixer.close()
        
        # once the stop event is set, return the recorded audio
        return frames