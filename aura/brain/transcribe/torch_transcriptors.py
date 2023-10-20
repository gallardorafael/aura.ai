import logging
from typing import Optional

import torch
from transformers import pipeline

from aura.utils import is_torch_available

from .transcriptor import Transcriptor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HugginFaceWhisperTranscriptor(Transcriptor):
    def __init__(
        self,
        model_name: Optional[str] = "openai/whisper-large-v2",
        half_precision: Optional[bool] = True,
    ):

        super().__init__()

        # type to be used
        torch_dtype = torch.float32
        if half_precision:
            torch_dtype = torch.float16

        # checking if torch is available
        if not is_torch_available:
            raise ImportError(f"torch must be installed in order to use a {self.__class__.name}")

        # checking if a GPU is available
        if not torch.cuda.is_available():
            raise RuntimeError("A CUDA capable device must be available to use a {self.__class__.name}")

        self.pipeline = pipeline(
            task="automatic-speech-recognition",
            model=model_name,
            torch_dtype=torch_dtype,
            device="cuda:0",
        )

        # converting model to BetterTransformer
        self.pipeline.model = self.pipeline.model.to_bettertransformer()

    def transcribe(self, audio_path):
        raw_outputs = self.pipeline(audio_path, chunk_length_s=30, batch_size=4, return_timestamps=True)

        return self._postprocess(raw_outputs)

    def detect_language(self, audio_path):
        raise NotImplementedError

    def _postprocess(self, raw_output: dict):
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
        return raw_output
