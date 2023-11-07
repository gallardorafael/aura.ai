import argparse
import logging

from aura.brain.transcribe import HugginFaceWhisperTranscriptor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(args):
    logger.info("Loading aura.ai transcriptors...")
    transcriptor = HugginFaceWhisperTranscriptor()
    logger.info("Transcriptors are ready!")

    logger.info(f"Transcribing audio {args.input_filepath} using {transcriptor.__class__.__name__}")
    outputs = transcriptor.transcribe(args.input_filepath)

    print(outputs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic transcription of an audio file.")
    parser.add_argument(
        "-i",
        "--input-filepath",
        type=str,
        required=True,
        help="Path to the audio file to be transcribed.",
    )
    parser.add_argument(
        "-o", "--output-filepath", type=str, required=False, help="Path to the output file."
    )
    args = parser.parse_args()

    main(args)
