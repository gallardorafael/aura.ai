import os
import threading
import uuid
from pathlib import Path

import numpy as np
import soundcard as sc

from aura.file_manager import AudioWriter
from aura.hear import DeviceExplorer

# TODO: create a path when installing aura, for configs and records
cwd = os.getcwd()

# TODO: make AudioRecorder manage threads instead of being a thread
class AudioRecorder:
    def __init__(self):
        super().__init__()
        self.stop_event = threading.Event()
        self.event_uuid = str(uuid.uuid4())
        self.root_path = Path(cwd) / "aura_records"
        self.device_explorer = DeviceExplorer()

        # threads for recording audio
        self.mic_thread = None
        self.system_thread = None

        # storage for audio frames
        self.mic_frames = []
        self.system_frames = []

        # flag for checking status
        self.recording = False

        # TODO: make this configurable
        self.audio_config = {
            "framerate": 44100,
            "frames_per_buffer": 1024,
        }

    def start_recording(self):
        self.recording = True
        # creating the threads for recording audio
        self.mic_thread = threading.Thread(target=self._record_from_mic)
        self.system_thread = threading.Thread(target=self._record_from_system)

        # start the threads
        self.mic_thread.start()
        self.system_thread.start()

    def stop_recording(self):
        self.recording = False
        if self.mic_thread:
            self.mic_thread.join()
        if self.system_thread:
            self.system_thread.join()

        self._mix_and_save()

    def _record_from_mic(self):
        with sc.default_microphone().recorder(samplerate=self.audio_config["framerate"]) as mic:
            while self.recording:
                # record audio from default microphone.
                self.mic_frames.extend(mic.record(numframes=self.audio_config["frames_per_buffer"]))

    def _record_from_system(self):
        with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
            samplerate=self.audio_config["framerate"]
        ) as mic:
            while self.recording:
                # record audio from a loopback device from default speaker.
                self.system_frames.extend(mic.record(numframes=self.audio_config["frames_per_buffer"]))

    def _mix_and_save(self):
        self.mic_frames = np.array(self.mic_frames)
        self.system_frames = np.array(self.system_frames)

        # mixing the audio from the two sources
        mixed_data = (self.mic_frames + self.system_frames) / 2

        # save the mixed audio to a file with AudioWriter
        writer = AudioWriter(self.root_path)
        writer.write(self.event_uuid, mixed_data, framerate=self.audio_config["framerate"])
