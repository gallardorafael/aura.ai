import datetime
import soundfile
from pathlib import Path

class AudioWriter:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.today = datetime.date.today().strftime("%Y-%m-%d")

    def write(self, filename, data, **kwargs):
        filepath = self._get_filename(filename)
        soundfile.write(str(filepath),
                        data, 
                        samplerate=kwargs['framerate'],
                        )

    def _get_filename(self, filename):
        directory = self.root_path / self.today
        if not directory.exists():
            directory.mkdir(parents=True)
        filepath = directory / Path(filename).with_suffix('.flac')
        return filepath