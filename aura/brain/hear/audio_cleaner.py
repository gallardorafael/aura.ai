import noisereduce as nr


class AudioCleaner:
    def __init__(self):
        super().__init__()

    def clean(self):
        raise NotImplementedError


class SpectralGatingAudioCleaner(AudioCleaner):
    def __init__(self, prop_decrease=0.5, stationary=True):
        """Class that implements the Spectral Gating Audio Cleaner with noisereduce library.

        Args:
            prop_decrease: proportion of the noise to be removed
            stationary: whether to use Stationary of Non-Stationary Noise Reduction
        """
        super().__init__()
        self.stationary = stationary
        self.prop_decrease = prop_decrease

    def clean(self, audio_data, sample_rate):
        return nr.reduce_noise(
            y=audio_data, sr=sample_rate, stationary=self.stationary, prop_decrease=self.prop_decrease
        )
