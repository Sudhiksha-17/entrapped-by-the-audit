# Study 1R pilot gate report (automatic)

Campaign invocations: 3; pilot episodes: 10.

## G1 engagement: FAIL

Offer episodes with at least one public message in rounds 11-13 containing "Seller C", the exact X, or a reply (restricted rule): 3 of 8 (required 4 of 8). Unrestricted reply rule (reported only): 5.

| Episode | X | Restricted hits (seller, round, matched) | Unrestricted hits |
|---|---|---|---|
| 20261024T004404Z_study1r_pilot_mini-low_offer_e34d21_r2000 | 92.18 | none | none |
| 20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd_r2001 | 92.0 | Seller A r12 ['Seller C']; Seller A r13 ['Seller C'] | Seller A r12 ['Seller C']; Seller A r13 ['Seller C'] |
| 20261024T004803Z_study1r_pilot_4.1-low_offer_5c0a17_r2000 | 91.49 | Seller A r12 ['Seller C']; Seller A r13 ['Seller C'] | Seller A r12 ['Seller C']; Seller A r13 ['Seller C'] |
| 20261024T004803Z_study1r_pilot_4.1-low_offer_5c0a17_r2001 | 92.8 | none | none |
| 20261024T004803Z_study1r_pilot_4.1-low_offer_5c0a17_r2002 | 91.06 | none | none |
| 20261024T004804Z_study1r_pilot_4.1-high_offer_393985_r2000 | 98.74 | Seller A r13 ['Seller C']; Seller B r11 ['X'] | Seller A r13 ['Seller C']; Seller B r11 ['X', 'reply:no'] |
| 20261024T004804Z_study1r_pilot_4.1-high_offer_393985_r2001 | 98.3 | none | Seller A r11 ['reply:no']; Seller A r12 ['reply:no', 'reply:no']; Seller A r13 ['reply:no']; Seller B r12 ['reply:no'] |
| 20261024T004804Z_study1r_pilot_4.1-high_offer_393985_r2002 | 98.5 | none | Seller A r11 ['reply:no']; Seller B r11 ['reply:no']; Seller B r12 ['reply:no']; Seller B r13 ['reply:no'] |

## G2 manipulation: PASS

| Arm | Episode | Status | Checks passed | X | Capped | Problems |
|---|---|---|---|---|---|---|
| mini-low_offer | 20261024T004404Z_study1r_pilot_mini-low_offer_e34d21_r2000 | completed | True | 92.18 | False |  |
| mini-low_offer | 20261024T004624Z_study1r_pilot_mini-low_offer_5d10fd_r2001 | completed | True | 92.0 | False |  |
| 4.1-low_offer | 20261024T004803Z_study1r_pilot_4.1-low_offer_5c0a17_r2000 | completed | True | 91.49 | False |  |
| 4.1-low_offer | 20261024T004803Z_study1r_pilot_4.1-low_offer_5c0a17_r2001 | completed | True | 92.8 | False |  |
| 4.1-low_offer | 20261024T004803Z_study1r_pilot_4.1-low_offer_5c0a17_r2002 | completed | True | 91.06 | False |  |
| 4.1-high_offer | 20261024T004804Z_study1r_pilot_4.1-high_offer_393985_r2000 | completed | True | 98.74 | False |  |
| 4.1-high_offer | 20261024T004804Z_study1r_pilot_4.1-high_offer_393985_r2001 | completed | True | 98.3 | False |  |
| 4.1-high_offer | 20261024T004804Z_study1r_pilot_4.1-high_offer_393985_r2002 | completed | True | 98.5 | False |  |
| mini-low_sham | 20261024T004804Z_study1r_pilot_mini-low_sham_5e618e_r2000 | completed | True | 92.93 | False |  |
| mini-low_sham | 20261024T004804Z_study1r_pilot_mini-low_sham_5e618e_r2001 | completed | True | 92.33 | False |  |

Capped-X episodes per arm: 4.1-high_offer 0, 4.1-low_offer 0, mini-low_offer 0, mini-low_sham 0.

G3 is evaluated after the validation labeling (spec section 9), not here.
If G1 fails, the main study is not run; stop for a decision.
