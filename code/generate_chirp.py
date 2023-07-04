import numpy as np
import scipy.signal as sig

frev = 470000

def generate_afg_chirp(
        chirp_length_time = 0.001,
        turn_freq = frev,
        chirp_middle = frev*0.325,
        chirp_dev = frev*0.025,
        sampling_freq = 1e9):
    """
    Generates a frequency-modulated single chirp signal, centered on `chirp_middle` [Hz], with a deviation of `chirp_dev` [Hz], and a length of `chirp_length_time` [s].
    """

    chirp_time_samples = np.arange(0, chirp_length_time, 1/sampling_freq)
    chirp_signal_samples = sig.chirp(chirp_time_samples,      # time array
                                     chirp_middle-chirp_dev,  # start frequency
                                     chirp_length_time,       # end time
                                     chirp_middle+chirp_dev)  # end frequency

    chirp_lasts_for_turns = chirp_length_time * turn_freq

    return chirp_time_samples, chirp_signal_samples, chirp_lasts_for_turns