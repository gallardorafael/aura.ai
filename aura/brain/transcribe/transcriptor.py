from abc import ABC, abstractmethod


class Transcriptor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def transcribe(self):
        """
        Function that receives the path of an audio file, then it transcribes the audio file and postprocess the text, in order to return a list of dictionaries
        with the following structure:
            {
                "speaker_id": "speaker_id",
                "text": "text of the transcription",
                "start_time": 0.0,
                "end_time": 1.0
            }
        The list will be ordered by the start_time of the transcription.
        """
        ...

    @abstractmethod
    def detect_language(self):
        ...

    @abstractmethod
    def _preprocess():
        ...

    @abstractmethod
    def _postprocess():
        ...
