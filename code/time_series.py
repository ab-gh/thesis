t = (particles.at_turn*t_rev) - particles.zeta/rel_beta/sp.constants.c

max_time = t.max()
sample_rate = 18000
total_samples = int(max_time * sample_rate) + 1 

time_series_data = np.zeros(total_samples)
arrival_indices = np.floor(t * sample_rate).astype(int)
for idx in arrival_indices:
    time_series_data[idx] += 1