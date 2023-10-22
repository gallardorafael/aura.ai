import logging
from typing import List, Optional

from pywhispercpp.model import Model, Segment

from .transcriptor import Transcriptor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PyWhisperCPPTranscriptor(Transcriptor):
    def __init__(
        self, model_name: Optional[str] = "medium.en", language: Optional[str] = "en", **kwargs
    ):

        super().__init__()

        self.model_name = model_name
        self.language = language
        self.model = Model(self.model_name, language=self.language, **kwargs)

    def transcribe(self, audio_path, **kwargs):
        raw_outputs = self.model.transcribe(audio_path, **kwargs)

        return self._postprocess(raw_outputs)

    def detect_language(self, audio_path):
        raise NotImplementedError

    def _postprocess(self, raw_output: List[Segment]):
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
        processed_output = []
        for output in raw_output:
            # processed_output.append({
            #     "speaker_id": "uuid",
            #     "text": output.text,
            #     "start_time": output.t0,
            #     "end_time": output.t1,
            # })
            processed_output.append(output.text)

        return processed_output
