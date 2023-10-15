import whisper


class Transcriptor:
    def __init__(self):
        super().__init__()

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

        raise NotImplementedError

    def detect_language(self):
        raise NotImplementedError

    def _postprocess():
        raise NotImplementedError


class WhisperTranscriptor(Transcriptor):
    def __init__(self, model_path=None):
        super().__init__()
        self.model = whisper.load_model(model_path)

    def transcribe(self, audio_path):
        whisper_output = self.model.transcribe(audio_path)
        return self._postprocess(whisper_output)

    def detect_language(self, audio_path):
        raise NotImplementedError

    def load_model(self, model_path):
        raise NotImplementedError

    def _postprocess(whisper_output: dict):
        """
        Function that postprocess the output of the whisper model, in order to return a list of dictionaries
        with the following structure:
            {
                "speaker_id": "speaker_id",
                "text": "text of the transcription",
                "start_time": 0.0,
                "end_time": 1.0
            }
        The list will be ordered by the start_time of the transcription.
        """
