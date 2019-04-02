import pickle

with open('./stats/kbox_stats/stats/elmo_gru_noise_drop_adv/elmo_gru_noise_drop_adv_eval_stats_ep5.pkl', 'rb') as f:
    p, r, f = data_to_dump = pickle.load(f)
    # data_to_dump = [precis, recall, f1_score]
    max_f = max(f)
    max_idx = f.index(max_f)

print(p[max_idx], r[max_idx], f[max_idx])
