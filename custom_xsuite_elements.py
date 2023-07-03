# TFB kicker

exciter_kick = kick_angle(float(gain))
F_rev = 1/twiss_parameters['T_rev0']

chirp_time, chirp_signal, chirp_n_turns = signal_gen.generate_afg_chirp(
    chirp_rep_time = interval*MS_TO_S,
    turn_freq = F_rev,
    chirp_middle = FREV * 0.325,
    chirp_dev = FREV * 0.025,
    sampling_freq = 1e9
)

exciter = xt.Exciter(
    samples = chirp_signal,
    sampling_frequency = 1e9,
    frev = F_rev,
    duration = 0.5,
    start_turn = 0,
    knl = [exciter_kick]
)
line.insert_element(
    element = exciter,
    name = 'EXCITER',
    index = 'pr.kfb97'
)

# Septum

septum = xt.LimitRect(
    min_x = -60*0.001 # meters
)
line.insert_element(
    element = septum,
    name = 'SEPTUM',
    index = 'pe.smh57'
)

# RF Cavity

rf_cavity = xt.Cavity(
    voltage = 130e3, # volts
    frequency = F_rev * 8, # Hz, 8th harmonic
    lag = 0
)
line.insert_element(
    element = rf_cavity,
    name = 'RFCAVITY',
    at_s = 0
)