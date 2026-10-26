# Study 1R results

## Excluded episodes (post-freeze deviation, I-056)

Post-freeze deviation (bug fix, I-056): the frozen results script did not apply the preregistered rule that failed episodes are excluded and replaced. This run used `scripts/study1r_results_completed.py`, which passes only completed episodes to the frozen analysis; no frozen file was modified.

- `20261024T091014Z_study1r_mini-low_anchor_a761c2_r028` (mini-low_anchor): status failed, failure reason other; replaced by `20261024T091014Z_study1r_mini-low_anchor_a761c2_r028_repl1` (completed)

Episodes: 351; arms: 4.1-high/offer, 4.1-high/silent, 4.1-low/anchor, 4.1-low/offer, 4.1-low/silent, mini-low/anchor, mini-low/offer, mini-low/sham, mini-low/silent.

Errors: 0. Skipped (arms absent): 0.

## T1 primary (mini-low Offer minus Anchor, change score)

```json
{
 "estimate": 0.23157083333333284,
 "ci_low": -0.18319437500000388,
 "ci_high": 0.6609523958333335,
 "level": 0.95,
 "p_bootstrap": 0.2838,
 "n_a": 60,
 "n_b": 60,
 "excludes_zero": false,
 "verdict": "not supported"
}
```

## T1 secondary, Holm family of five (permutation p)

```json
{
 "mini-low Offer minus Sham": {
  "estimate": 0.80662840909091,
  "ci_low": 0.3320709943181835,
  "ci_high": 1.269961619318181,
  "level": 0.95,
  "p_bootstrap": 0.0006,
  "n_a": 60,
  "n_b": 33,
  "excludes_zero": true,
  "p_permutation": 0.0025997400259974,
  "p_holm": 0.012998700129987
 },
 "mini-low Anchor minus Sham": {
  "estimate": 0.5750575757575772,
  "ci_low": 0.17145825757575972,
  "ci_high": 0.9734107765151523,
  "level": 0.95,
  "p_bootstrap": 0.0058,
  "n_a": 60,
  "n_b": 33,
  "excludes_zero": true,
  "p_permutation": 0.007799220077992201,
  "p_holm": 0.031196880311968805
 },
 "mini-low Sham minus Silent": {
  "estimate": -0.11845454545454609,
  "ci_low": -0.5212062500000023,
  "ci_high": 0.28533750000000024,
  "level": 0.95,
  "p_bootstrap": 0.563,
  "n_a": 33,
  "n_b": 33,
  "excludes_zero": false,
  "p_permutation": 0.5808419158084192,
  "p_holm": 1.0
 },
 "4.1-low Offer minus Anchor (secondary T1)": {
  "estimate": 0.07149999999999823,
  "ci_low": -0.4752481060606087,
  "ci_high": 0.6377933712121144,
  "level": 0.95,
  "p_bootstrap": 0.8306,
  "n_a": 33,
  "n_b": 33,
  "excludes_zero": false,
  "p_permutation": 0.8066193380661933,
  "verdict": "not supported",
  "p_holm": 1.0
 },
 "4.1-high Offer minus Silent (disruption)": {
  "estimate": 0.25989393939393973,
  "ci_low": 0.024157575757576783,
  "ci_high": 0.496937310606062,
  "level": 0.95,
  "p_bootstrap": 0.032,
  "n_a": 33,
  "n_b": 33,
  "excludes_zero": true,
  "p_permutation": 0.0374962503749625,
  "verdict": "opposite direction",
  "p_holm": 0.1124887511248875
 }
}
```

## Disruption in mini-low and 4.1-low (descriptive)

```json
{
 "mini-low Offer minus Silent (disruption, descriptive)": {
  "estimate": 0.6881738636363639,
  "ci_low": 0.2600242329545456,
  "ci_high": 1.1141840625000017,
  "level": 0.95,
  "p_bootstrap": 0.0018,
  "n_a": 60,
  "n_b": 33,
  "excludes_zero": true
 },
 "4.1-low Offer minus Silent (disruption, descriptive)": {
  "estimate": 0.19112878787878906,
  "ci_low": -0.41184185606060353,
  "ci_high": 0.8765367424242438,
  "level": 0.95,
  "p_bootstrap": 0.5558,
  "n_a": 33,
  "n_b": 33,
  "excludes_zero": false
 }
}
```

## T1 secondary, ANCOVA (uncorrected)

```json
{
 "offer_coef": 0.24212873014757047,
 "se_hc3": 0.2252289778469095,
 "ci_low": -0.19931195470714186,
 "ci_high": 0.6835694150022829,
 "pre_coef": 0.9481608994603958,
 "n": 120
}
```

## T1 secondary, Fisher on the behavioral flag (uncorrected)

```json
{
 "table": [
  [
   3,
   57
  ],
  [
   2,
   58
  ]
 ],
 "odds_ratio": 1.5263157894736843,
 "p_value": 1.0
}
```

## T2a primary (inclusive, rounds 11-30)

```json
{
 "estimate": 0.30303030303030304,
 "ci_low": 0.12121212121212122,
 "ci_high": 0.48484848484848486,
 "level": 0.95,
 "p_bootstrap": 0.0024,
 "n_a": 33,
 "n_b": 33,
 "excludes_zero": true,
 "measure": "acc_inclusive",
 "verdict": "supported"
}
```

## T2a secondary (strict; lower bound under the stopping rule)

```json
{
 "estimate": 0.24242424242424243,
 "ci_low": 0.12121212121212122,
 "ci_high": 0.3939393939393939,
 "level": 0.95,
 "p_bootstrap": 0.0,
 "n_a": 33,
 "n_b": 33,
 "excludes_zero": true,
 "measure": "acc_strict",
 "verdict": "supported"
}
```

## T2a sensitivity (inclusive, rounds 11-12; lower bound under the stopping rule)

```json
{
 "estimate": -0.030303030303030304,
 "ci_low": -0.09090909090909091,
 "ci_high": 0.0,
 "level": 0.95,
 "p_bootstrap": 0.7276,
 "n_a": 33,
 "n_b": 33,
 "excludes_zero": false,
 "measure": "acc_inclusive_11_12",
 "verdict": "not supported"
}
```

## T2a sensitivity, corrected for the estimated miss rate

```json
{
 "estimate": 0.30303030303030304,
 "ci_low": 0.12121212121212122,
 "ci_high": 0.48484848484848486,
 "excludes_zero": true,
 "rate_high": 0.36363636363636365,
 "rate_low": 0.06060606060606061,
 "n_high": 33,
 "n_low": 33,
 "p_audit_flagged": 0.0,
 "p_audit_unflagged": 0.0,
 "measure": "inclusive acceptance corrected for the estimated miss rate",
 "verdict": "supported"
}
```

## Miss audit (option A; secondary)

```json
{
 "strata": {
  "audit_flagged": {
   "audited": 23,
   "accepted": 0,
   "rate": 0.0,
   "ci": [
    0.0,
    0.14311661845042686
   ],
   "screener_negatives": 227,
   "uncoded": 204
  },
  "audit_unflagged": {
   "audited": 50,
   "accepted": 0,
   "rate": 0.0,
   "ci": [
    6.938893903907228e-18,
    0.07134759913335872
   ],
   "screener_negatives": 2251,
   "uncoded": 2201
  }
 },
 "weighted_miss_rate": {
  "rate": 0.0,
  "ci": [
   0.0,
   0.0
  ]
 },
 "expected_missed_acceptance_messages": 0.0,
 "verification": {
  "messages": 162,
  "uncoded": 0,
  "coded": 162,
  "accepting_episodes": 14
 },
 "audit_accepting_episodes_not_in_primary": 0
}
```

## T2a secondary, logistic regression on cell and jump

```json
{
 "n": 66,
 "converged": true,
 "separation_suspected": false,
 "coefficients": {
  "intercept": {
   "estimate": 1.09942989001087,
   "se": 3.800961139534254,
   "ci_low": -6.350317050112591,
   "ci_high": 8.549176830134332
  },
  "cell_4.1-high": {
   "estimate": -0.747067649091588,
   "se": 2.9202367518186736,
   "ci_low": -6.47062650898642,
   "ci_high": 4.976491210803244
  },
  "jump": {
   "estimate": -0.5614986551356351,
   "se": 0.5726982083092419,
   "ci_low": -1.6839665174323668,
   "ci_high": 0.5609692071610966
  }
 }
}
```

## T2a sensitivity, alternative coding (inclusive)

```json
{
 "estimate": 0.30303030303030304,
 "ci_low": 0.12121212121212122,
 "ci_high": 0.48484848484848486,
 "level": 0.95,
 "p_bootstrap": 0.0024,
 "n_a": 33,
 "n_b": 33,
 "excludes_zero": true,
 "measure": "acc_inclusive_alt",
 "verdict": "supported"
}
```

## T2a sensitivity, alternative coding (strict; lower bound)

```json
{
 "estimate": 0.24242424242424243,
 "ci_low": 0.12121212121212122,
 "ci_high": 0.3939393939393939,
 "level": 0.95,
 "p_bootstrap": 0.0,
 "n_a": 33,
 "n_b": 33,
 "excludes_zero": true,
 "measure": "acc_strict_alt",
 "verdict": "supported"
}
```

## Alternative coding: reclassified messages (sensitivity)

```json
{
 "4.1-low": {
  "episodes": 33,
  "reclassified_messages": 9
 },
 "4.1-high": {
  "episodes": 33,
  "reclassified_messages": 12
 }
}
```

## T2b per cell (secondary)

```json
{
 "mini-low": {
  "excess": {
   "estimate": 0.0196969696969697,
   "ci_low": -0.06060606060606061,
   "ci_high": 0.1,
   "level": 0.95,
   "p_bootstrap": 0.5678,
   "n_a": 60,
   "n_b": 33,
   "excludes_zero": false
  },
  "natural_rate": 0.030303030303030304,
  "natural_rate_ci": [
   0.00536941053687183,
   0.1531872538211892
  ]
 },
 "4.1-low": {
  "excess": {
   "estimate": 0.0,
   "ci_low": 0.0,
   "ci_high": 0.0,
   "level": 0.95,
   "p_bootstrap": 1.0,
   "n_a": 33,
   "n_b": 33,
   "excludes_zero": false
  },
  "natural_rate": 0.0,
  "natural_rate_ci": [
   0.0,
   0.10426999754245206
  ]
 },
 "4.1-high": {
  "excess": {
   "estimate": 0.030303030303030304,
   "ci_low": 0.0,
   "ci_high": 0.09090909090909091,
   "level": 0.95,
   "p_bootstrap": 0.7246,
   "n_a": 33,
   "n_b": 33,
   "excludes_zero": false
  },
  "natural_rate": 0.0,
  "natural_rate_ci": [
   0.0,
   0.10426999754245206
  ]
 }
}
```

## Compliance table (secondary)

```json
{
 "mini-low": {
  "skipped": "no Offer episodes with verbal labels in mini-low"
 },
 "4.1-low": {
  "table": {
   "V+B+": 0,
   "V+B-": 2,
   "V-B+": 0,
   "V-B-": 31
  },
  "n": 33,
  "accepts_without_behavioral_movement": 1.0,
  "ci_low": 0.34238022750665303,
  "ci_high": 1.0
 },
 "4.1-high": {
  "table": {
   "V+B+": 1,
   "V+B-": 11,
   "V-B+": 0,
   "V-B-": 21
  },
  "n": 33,
  "accepts_without_behavioral_movement": 0.9166666666666666,
  "ci_low": 0.646120088858883,
  "ci_high": 0.9851349055950829
 }
}
```

## Calibration table (secondary)

```json
{
 "mini-low": {
  "silent_n": 33,
  "offer_n": 60,
  "propensity_91.80": 0.030303030303030304,
  "propensity_92.70": 0.030303030303030304,
  "propensity_94.50": 0.0,
  "silent_mean_post": 85.24561363636364,
  "offer_acc_inclusive": null,
  "offer_behavioral_acceptance": 0.05
 },
 "4.1-low": {
  "silent_n": 33,
  "offer_n": 33,
  "propensity_91.80": 0.030303030303030304,
  "propensity_92.70": 0.0,
  "propensity_94.50": 0.0,
  "silent_mean_post": 84.69150757575758,
  "offer_acc_inclusive": 0.06060606060606061,
  "offer_behavioral_acceptance": 0.0
 },
 "4.1-high": {
  "silent_n": 33,
  "offer_n": 33,
  "propensity_91.80": 1.0,
  "propensity_92.70": 1.0,
  "propensity_94.50": 1.0,
  "silent_mean_post": 96.32021212121212,
  "offer_acc_inclusive": 0.36363636363636365,
  "offer_behavioral_acceptance": 0.030303030303030304
 }
}
```

## Awareness probe (secondary; aware acceptance a lower bound under the stopping rule)

```json
{
 "per_arm": {
  "4.1-high/offer": {
   "sellers": 66,
   "yes": 66,
   "unparseable": 0,
   "rate": 1.0,
   "ci": [
    0.9449974429864586,
    0.9999999999999999
   ]
  },
  "4.1-high/silent": {
   "sellers": 66,
   "yes": 66,
   "unparseable": 0,
   "rate": 1.0,
   "ci": [
    0.9449974429864586,
    0.9999999999999999
   ]
  },
  "4.1-low/anchor": {
   "sellers": 66,
   "yes": 66,
   "unparseable": 0,
   "rate": 1.0,
   "ci": [
    0.9449974429864586,
    0.9999999999999999
   ]
  },
  "4.1-low/offer": {
   "sellers": 66,
   "yes": 65,
   "unparseable": 0,
   "rate": 0.9848484848484849,
   "ci": [
    0.9190407973793359,
    0.9973203594560177
   ]
  },
  "4.1-low/silent": {
   "sellers": 66,
   "yes": 65,
   "unparseable": 0,
   "rate": 0.9848484848484849,
   "ci": [
    0.9190407973793359,
    0.9973203594560177
   ]
  },
  "mini-low/anchor": {
   "sellers": 120,
   "yes": 59,
   "unparseable": 0,
   "rate": 0.49166666666666664,
   "ci": [
    0.4038757172769723,
    0.5799746021633394
   ]
  },
  "mini-low/offer": {
   "sellers": 120,
   "yes": 89,
   "unparseable": 0,
   "rate": 0.7416666666666667,
   "ci": [
    0.6567146994175665,
    0.8116260368133936
   ]
  },
  "mini-low/sham": {
   "sellers": 66,
   "yes": 40,
   "unparseable": 0,
   "rate": 0.6060606060606061,
   "ci": [
    0.4854840080039292,
    0.7149699950538045
   ]
  },
  "mini-low/silent": {
   "sellers": 66,
   "yes": 48,
   "unparseable": 0,
   "rate": 0.7272727272727273,
   "ci": [
    0.6095777422224589,
    0.8199665500441133
   ]
  }
 },
 "offer_minus_silent": {
  "mini-low": {
   "estimate": 0.014393939393939403,
   "ci_low": -0.11818181818181828,
   "ci_high": 0.14848484848484855,
   "level": 0.95,
   "p_bootstrap": 0.8594,
   "n_a": 120,
   "n_b": 66,
   "excludes_zero": false
  },
  "4.1-low": {
   "estimate": 0.0,
   "ci_low": -0.045454545454545414,
   "ci_high": 0.045454545454545414,
   "level": 0.95,
   "p_bootstrap": 1.0,
   "n_a": 66,
   "n_b": 66,
   "excludes_zero": false
  },
  "4.1-high": {
   "estimate": 0.0,
   "ci_low": 0.0,
   "ci_high": 0.0,
   "level": 0.95,
   "p_bootstrap": 1.0,
   "n_a": 66,
   "n_b": 66,
   "excludes_zero": false
  }
 },
 "aware_acceptance": {
  "mini-low": {
   "sellers": 120,
   "aware_acceptance": 0,
   "share": 0.0,
   "episodes": 60,
   "aware_accepting_episodes": 0
  },
  "4.1-low": {
   "sellers": 66,
   "aware_acceptance": 3,
   "share": 0.045454545454545456,
   "episodes": 33,
   "aware_accepting_episodes": 2
  },
  "4.1-high": {
   "sellers": 66,
   "aware_acceptance": 14,
   "share": 0.21212121212121213,
   "episodes": 33,
   "aware_accepting_episodes": 12
  }
 }
}
```

## Round of first engagement (descriptive; detector- and screener-based)

```json
{
 "mini-low (detector)": {
  "basis": "detector",
  "curve": [
   {
    "round": 11,
    "at_risk": 60,
    "first_engaged": 9,
    "cumulative_engaged_share": 0.15000000000000002
   },
   {
    "round": 12,
    "at_risk": 51,
    "first_engaged": 6,
    "cumulative_engaged_share": 0.25
   },
   {
    "round": 13,
    "at_risk": 45,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.30000000000000004
   },
   {
    "round": 14,
    "at_risk": 42,
    "first_engaged": 5,
    "cumulative_engaged_share": 0.3833333333333334
   },
   {
    "round": 15,
    "at_risk": 37,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.43333333333333346
   },
   {
    "round": 16,
    "at_risk": 34,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.4833333333333335
   },
   {
    "round": 17,
    "at_risk": 31,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4833333333333335
   },
   {
    "round": 18,
    "at_risk": 31,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4833333333333335
   },
   {
    "round": 19,
    "at_risk": 31,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.5166666666666668
   },
   {
    "round": 20,
    "at_risk": 29,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.5666666666666668
   },
   {
    "round": 21,
    "at_risk": 26,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5666666666666668
   },
   {
    "round": 22,
    "at_risk": 26,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5666666666666668
   },
   {
    "round": 23,
    "at_risk": 26,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.5833333333333335
   },
   {
    "round": 24,
    "at_risk": 25,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6000000000000001
   },
   {
    "round": 25,
    "at_risk": 24,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6000000000000001
   },
   {
    "round": 26,
    "at_risk": 24,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6166666666666667
   },
   {
    "round": 27,
    "at_risk": 23,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6166666666666667
   },
   {
    "round": 28,
    "at_risk": 23,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6333333333333334
   },
   {
    "round": 29,
    "at_risk": 22,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6333333333333334
   },
   {
    "round": 30,
    "at_risk": 22,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6500000000000001
   }
  ]
 },
 "mini-low (judge v2 screener)": {
  "basis": "judge v2 screener",
  "curve": [
   {
    "round": 11,
    "at_risk": 60,
    "first_engaged": 8,
    "cumulative_engaged_share": 0.1333333333333333
   },
   {
    "round": 12,
    "at_risk": 52,
    "first_engaged": 5,
    "cumulative_engaged_share": 0.21666666666666667
   },
   {
    "round": 13,
    "at_risk": 47,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.2833333333333333
   },
   {
    "round": 14,
    "at_risk": 43,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.33333333333333337
   },
   {
    "round": 15,
    "at_risk": 40,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.3666666666666667
   },
   {
    "round": 16,
    "at_risk": 38,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.4
   },
   {
    "round": 17,
    "at_risk": 36,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.41666666666666674
   },
   {
    "round": 18,
    "at_risk": 35,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.4666666666666668
   },
   {
    "round": 19,
    "at_risk": 32,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.4833333333333334
   },
   {
    "round": 20,
    "at_risk": 31,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.5166666666666667
   },
   {
    "round": 21,
    "at_risk": 29,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5166666666666667
   },
   {
    "round": 22,
    "at_risk": 29,
    "first_engaged": 0,
    "cumulative_engaged_s
```

## Exploratory (test suspicion, acceptance by round as a lower bound, ACK rates)

```json
{
 "public_private_gap": {},
 "test_suspicion": {
  "4.1-high/offer": 0.0,
  "4.1-low/offer": 0.0
 },
 "ack_rate": {
  "4.1-high/offer": 0.3237639553429027,
  "4.1-low/anchor": 0.43460925039872406,
  "4.1-low/offer": 0.17543859649122806,
  "mini-low/anchor": 0.08114035087719298,
  "mini-low/offer": 0.24298245614035088,
  "mini-low/sham": 0.013556618819776713
 },
 "acceptance_by_round": {
  "4.1-low": {
   "11": 0.030303030303030304,
   "12": 0.0,
   "13": 0.0,
   "14": 0.0,
   "15": 0.030303030303030304,
   "16": 0.0,
   "17": 0.0,
   "18": 0.0,
   "19": 0.0,
   "20": 0.0,
   "21": 0.0,
   "22": 0.030303030303030304,
   "23": 0.0,
   "24": 0.0,
   "25": 0.0,
   "26": 0.030303030303030304,
   "27": 0.0,
   "28": 0.0,
   "29": 0.030303030303030304,
   "30": 0.0
  },
  "4.1-high": {
   "11": 0.0,
   "12": 0.0,
   "13": 0.0,
   "14": 0.0,
   "15": 0.0,
   "16": 0.0,
   "17": 0.06060606060606061,
   "18": 0.030303030303030304,
   "19": 0.0,
   "20": 0.06060606060606061,
   "21": 0.06060606060606061,
   "22": 0.030303030303030304,
   "23": 0.0,
   "24": 0.030303030303030304,
   "25": 0.030303030303030304,
   "26": 0.06060606060606061,
   "27": 0.06060606060606061,
   "28": 0.0,
   "29": 0.06060606060606061,
   "30": 0.15151515151515152
  }
 }
}
```

## Pre-enumerated outcomes (descriptive)

```json
{
 "compression": {
  "t2a": {
   "estimate": 0.30303030303030304,
   "ci_low": 0.12121212121212122,
   "ci_high": 0.48484848484848486,
   "level": 0.95,
   "p_bootstrap": 0.0024,
   "n_a": 33,
   "n_b": 33,
   "excludes_zero": true,
   "measure": "acc_inclusive",
   "verdict": "supported"
  },
  "propensity_difference_silent": {
   "estimate": 1.0,
   "ci_low": 1.0,
   "ci_high": 1.0,
   "level": 0.95,
   "p_bootstrap": 0.0,
   "n_a": 33,
   "n_b": 33,
   "excludes_zero": true
  },
  "compression": false
 },
 "anchoring_dominance": {
  "offer_minus_sham": {
   "estimate": 0.80662840909091,
   "ci_low": 0.3320709943181835,
   "ci_high": 1.269961619318181,
   "level": 0.95,
   "p_bootstrap": 0.0006,
   "n_a": 60,
   "n_b": 33,
   "excludes_zero": true
  },
  "ratio": 0.7129151035055673,
  "ratio_ci": [
   0.2784040916690413,
   1.3470538468137807
  ],
  "anchoring_dominance": true
 },
 "says_yes_does_not_act": {
  "mini-low": {
   "skipped": "no Offer episodes with verbal labels in mini-low"
  },
  "4.1-low": {
   "table": {
    "V+B+": 0,
    "V+B-": 2,
    "V-B+": 0,
    "V-B-": 31
   },
   "n": 33,
   "accepts_without_behavioral_movement": 1.0,
   "ci_low": 0.34238022750665303,
   "ci_high": 1.0
  },
  "4.1-high": {
   "table": {
    "V+B+": 1,
    "V+B-": 11,
    "V-B+": 0,
    "V-B-": 21
   },
   "n": 33,
   "accepts_without_behavioral_movement": 0.9166666666666666,
   "ci_low": 0.646120088858883,
   "ci_high": 0.9851349055950829
  }
 },
 "ignoring": {
  "mini-low (judge v2 screener)": {
   "n": 60,
   "never_engaged": 20,
   "share": 0.3333333333333333,
   "ci": [
    0.2272926152352268,
    0.4594313354788031
   ]
  },
  "mini-low (detector)": {
   "n": 60,
   "never_engaged": 21,
   "share": 0.35,
   "ci": [
    0.24167774406017556,
    0.47637381158245135
   ]
  },
  "4.1-low (judge v2 screener)": {
   "n": 33,
   "never_engaged": 9,
   "share": 0.2727272727272727,
   "ci": [
    0.1506744088542064,
    0.44217559002872625
   ]
  },
  "4.1-low (detector)": {
   "n": 33,
   "never_engaged": 18,
   "share": 0.5454545454545454,
   "ci": [
    0.37985938536217456,
    0.7015706148612388
   ]
  },
  "4.1-high (judge v2 screener)": {
   "n": 33,
   "never_engaged": 0,
   "share": 0.0,
   "ci": [
    0.0,
    0.10426999754245206
   ]
  },
  "4.1-high (detector)": {
   "n": 33,
   "never_engaged": 1,
   "share": 0.030303030303030304,
   "ci": [
    0.00536941053687183,
    0.1531872538211892
   ]
  }
 }
}
```

## Judge comparison figure (exploratory: v1-read, v2-read, human-confirmed, behavioral)

```json
{
 "mini-low": {
  "v1_read": {
   "k": 37,
   "n": 60,
   "rate": 0.6166666666666667,
   "ci": [
    0.49017595824099924,
    0.7291172762591798
   ]
  },
  "v2_read": {
   "k": 2,
   "n": 60,
   "rate": 0.03333333333333333,
   "ci": [
    0.009189319256197877,
    0.113637742743086
   ]
  },
  "human_coded": {
   "k": 0,
   "n": 0,
   "rate": null,
   "ci": null
  },
  "behavioral_flag": {
   "k": 3,
   "n": 60,
   "rate": 0.05,
   "ci": [
    0.01714950216439568,
    0.1370051647634852
   ]
  }
 },
 "4.1-low": {
  "v1_read": {
   "k": 5,
   "n": 33,
   "rate": 0.15151515151515152,
   "ci": [
    0.06650457281607568,
    0.3091987588044212
   ]
  },
  "v2_read": {
   "k": 5,
   "n": 33,
   "rate": 0.15151515151515152,
   "ci": [
    0.06650457281607568,
    0.3091987588044212
   ]
  },
  "human_coded": {
   "k": 2,
   "n": 33,
   "rate": 0.06060606060606061,
   "ci": [
    0.016780883087191875,
    0.1960624480864781
   ]
  },
  "behavioral_flag": {
   "k": 0,
   "n": 33,
   "rate": 0.0,
   "ci": [
    0.0,
    0.10426999754245206
   ]
  }
 },
 "4.1-high": {
  "v1_read": {
   "k": 32,
   "n": 33,
   "rate": 0.9696969696969697,
   "ci": [
    0.846812746178811,
    0.9946305894631283
   ]
  },
  "v2_read": {
   "k": 13,
   "n": 33,
   "rate": 0.3939393939393939,
   "ci": [
    0.2468310743447709,
    0.5631655918005977
   ]
  },
  "human_coded": {
   "k": 12,
   "n": 33,
   "rate": 0.36363636363636365,
   "ci": [
    0.2218717823524236,
    0.5338382169773361
   ]
  },
  "behavioral_flag": {
   "k": 1,
   "n": 33,
   "rate": 0.030303030303030304,
   "ci": [
    0.00536941053687183,
    0.1531872538211892
   ]
  }
 }
}
```

## Study 1R-A add-on (preregistered; run only on the entrant's approval)

```json
{
 "disruption": {
  "skipped": "no data for ('4.1-high', 'competitive')"
 },
 "propensity": {
  "silent": {
   "k": 33,
   "n": 33,
   "rate": 1.0,
   "ci": [
    0.895730002457548,
    1.0
   ]
  }
 }
}
```

## Labeler A vs Labeler B agreement (secondary; option A reliability, PREREG section 8)

From `scripts/study1r_backup_reliability.py agreement` (frozen).

```json
{
 "items": 32,
 "response": {
  "raw_agreement": 0.71875,
  "kappa": {
   "kappa": 0.6254876462938882,
   "ci_low": 0.4132029339853301,
   "ci_high": 0.8150355745731467,
   "n": 32
  }
 },
 "inclusive_acceptance": {
  "table": {
   "A accept / B accept": 14,
   "A accept / B not": 2,
   "A not / B accept": 2,
   "A not / B not": 14
  },
  "raw_agreement": 0.875,
  "kappa": {
   "kappa": 0.75,
   "ci_low": 0.49407114624505927,
   "ci_high": 0.9375,
   "n": 32
  }
 }
}
```

## Screener precision (exploratory, post hoc; not output by the frozen analysis)

Share of screener-positive messages human-coded accept or conditional_accept, on Labeler B's random 20% sample of the verification set (never dropped by the stopping rule).

```json
{
 "verification_messages": 162,
 "coded_by_labeler_a": 81,
 "dropped_by_stopping_rule": 81,
 "note": "the frozen miss audit's verification 'coded' count is messages minus uncoded, so it includes messages dropped by the stopping rule",
 "labeler_b_sample": 32,
 "precision_labeler_a_on_b_sample": {
  "k": 16,
  "n": 32,
  "rate": 0.5,
  "ci": [
   0.33630882869327483,
   0.6636911713067252
  ]
 },
 "precision_labeler_b": {
  "k": 16,
  "n": 32,
  "rate": 0.5,
  "ci": [
   0.33630882869327483,
   0.6636911713067252
  ]
 }
}
```

## Full output of sections truncated above (the frozen report cuts each at 4000 characters)

### Round of first engagement (descriptive; detector- and screener-based)

```json
{
 "mini-low (detector)": {
  "basis": "detector",
  "curve": [
   {
    "round": 11,
    "at_risk": 60,
    "first_engaged": 9,
    "cumulative_engaged_share": 0.15000000000000002
   },
   {
    "round": 12,
    "at_risk": 51,
    "first_engaged": 6,
    "cumulative_engaged_share": 0.25
   },
   {
    "round": 13,
    "at_risk": 45,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.30000000000000004
   },
   {
    "round": 14,
    "at_risk": 42,
    "first_engaged": 5,
    "cumulative_engaged_share": 0.3833333333333334
   },
   {
    "round": 15,
    "at_risk": 37,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.43333333333333346
   },
   {
    "round": 16,
    "at_risk": 34,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.4833333333333335
   },
   {
    "round": 17,
    "at_risk": 31,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4833333333333335
   },
   {
    "round": 18,
    "at_risk": 31,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4833333333333335
   },
   {
    "round": 19,
    "at_risk": 31,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.5166666666666668
   },
   {
    "round": 20,
    "at_risk": 29,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.5666666666666668
   },
   {
    "round": 21,
    "at_risk": 26,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5666666666666668
   },
   {
    "round": 22,
    "at_risk": 26,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5666666666666668
   },
   {
    "round": 23,
    "at_risk": 26,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.5833333333333335
   },
   {
    "round": 24,
    "at_risk": 25,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6000000000000001
   },
   {
    "round": 25,
    "at_risk": 24,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6000000000000001
   },
   {
    "round": 26,
    "at_risk": 24,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6166666666666667
   },
   {
    "round": 27,
    "at_risk": 23,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6166666666666667
   },
   {
    "round": 28,
    "at_risk": 23,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6333333333333334
   },
   {
    "round": 29,
    "at_risk": 22,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6333333333333334
   },
   {
    "round": 30,
    "at_risk": 22,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6500000000000001
   }
  ]
 },
 "mini-low (judge v2 screener)": {
  "basis": "judge v2 screener",
  "curve": [
   {
    "round": 11,
    "at_risk": 60,
    "first_engaged": 8,
    "cumulative_engaged_share": 0.1333333333333333
   },
   {
    "round": 12,
    "at_risk": 52,
    "first_engaged": 5,
    "cumulative_engaged_share": 0.21666666666666667
   },
   {
    "round": 13,
    "at_risk": 47,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.2833333333333333
   },
   {
    "round": 14,
    "at_risk": 43,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.33333333333333337
   },
   {
    "round": 15,
    "at_risk": 40,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.3666666666666667
   },
   {
    "round": 16,
    "at_risk": 38,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.4
   },
   {
    "round": 17,
    "at_risk": 36,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.41666666666666674
   },
   {
    "round": 18,
    "at_risk": 35,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.4666666666666668
   },
   {
    "round": 19,
    "at_risk": 32,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.4833333333333334
   },
   {
    "round": 20,
    "at_risk": 31,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.5166666666666667
   },
   {
    "round": 21,
    "at_risk": 29,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5166666666666667
   },
   {
    "round": 22,
    "at_risk": 29,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5166666666666667
   },
   {
    "round": 23,
    "at_risk": 29,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.5666666666666667
   },
   {
    "round": 24,
    "at_risk": 26,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.5833333333333334
   },
   {
    "round": 25,
    "at_risk": 25,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6000000000000001
   },
   {
    "round": 26,
    "at_risk": 24,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6166666666666667
   },
   {
    "round": 27,
    "at_risk": 23,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6166666666666667
   },
   {
    "round": 28,
    "at_risk": 23,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.65
   },
   {
    "round": 29,
    "at_risk": 21,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6666666666666667
   },
   {
    "round": 30,
    "at_risk": 20,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6666666666666667
   }
  ]
 },
 "4.1-low (detector)": {
  "basis": "detector",
  "curve": [
   {
    "round": 11,
    "at_risk": 33,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.12121212121212122
   },
   {
    "round": 12,
    "at_risk": 29,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.18181818181818188
   },
   {
    "round": 13,
    "at_risk": 27,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.21212121212121215
   },
   {
    "round": 14,
    "at_risk": 26,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.2727272727272727
   },
   {
    "round": 15,
    "at_risk": 24,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.36363636363636365
   },
   {
    "round": 16,
    "at_risk": 21,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.36363636363636365
   },
   {
    "round": 17,
    "at_risk": 21,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.36363636363636365
   },
   {
    "round": 18,
    "at_risk": 21,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.39393939393939403
   },
   {
    "round": 19,
    "at_risk": 20,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.39393939393939403
   },
   {
    "round": 20,
    "at_risk": 20,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.4242424242424243
   },
   {
    "round": 21,
    "at_risk": 19,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4242424242424243
   },
   {
    "round": 22,
    "at_risk": 19,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4242424242424243
   },
   {
    "round": 23,
    "at_risk": 19,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 24,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 25,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 26,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 27,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 28,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 29,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 30,
    "at_risk": 18,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.4545454545454546
   }
  ]
 },
 "4.1-low (judge v2 screener)": {
  "basis": "judge v2 screener",
  "curve": [
   {
    "round": 11,
    "at_risk": 33,
    "first_engaged": 7,
    "cumulative_engaged_share": 0.21212121212121215
   },
   {
    "round": 12,
    "at_risk": 26,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.33333333333333337
   },
   {
    "round": 13,
    "at_risk": 22,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.4242424242424243
   },
   {
    "round": 14,
    "at_risk": 19,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.4545454545454546
   },
   {
    "round": 15,
    "at_risk": 18,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.5757575757575758
   },
   {
    "round": 16,
    "at_risk": 14,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6060606060606061
   },
   {
    "round": 17,
    "at_risk": 13,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6363636363636364
   },
   {
    "round": 18,
    "at_risk": 12,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.6666666666666667
   },
   {
    "round": 19,
    "at_risk": 11,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6666666666666667
   },
   {
    "round": 20,
    "at_risk": 11,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6666666666666667
   },
   {
    "round": 21,
    "at_risk": 11,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.6666666666666667
   },
   {
    "round": 22,
    "at_risk": 11,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 23,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 24,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 25,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 26,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 27,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 28,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 29,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 30,
    "at_risk": 9,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7272727272727273
   }
  ]
 },
 "4.1-high (detector)": {
  "basis": "detector",
  "curve": [
   {
    "round": 11,
    "at_risk": 33,
    "first_engaged": 9,
    "cumulative_engaged_share": 0.2727272727272727
   },
   {
    "round": 12,
    "at_risk": 24,
    "first_engaged": 5,
    "cumulative_engaged_share": 0.4242424242424242
   },
   {
    "round": 13,
    "at_risk": 19,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.5151515151515151
   },
   {
    "round": 14,
    "at_risk": 16,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.5757575757575757
   },
   {
    "round": 15,
    "at_risk": 14,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.606060606060606
   },
   {
    "round": 16,
    "at_risk": 13,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 17,
    "at_risk": 9,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.7575757575757576
   },
   {
    "round": 18,
    "at_risk": 8,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7575757575757576
   },
   {
    "round": 19,
    "at_risk": 8,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.7575757575757576
   },
   {
    "round": 20,
    "at_risk": 8,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.7878787878787878
   },
   {
    "round": 21,
    "at_risk": 7,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.8181818181818181
   },
   {
    "round": 22,
    "at_risk": 6,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.9090909090909091
   },
   {
    "round": 23,
    "at_risk": 3,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 24,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 25,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 26,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 27,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 28,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 29,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 30,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9696969696969697
   }
  ]
 },
 "4.1-high (judge v2 screener)": {
  "basis": "judge v2 screener",
  "curve": [
   {
    "round": 11,
    "at_risk": 33,
    "first_engaged": 6,
    "cumulative_engaged_share": 0.18181818181818188
   },
   {
    "round": 12,
    "at_risk": 27,
    "first_engaged": 6,
    "cumulative_engaged_share": 0.36363636363636365
   },
   {
    "round": 13,
    "at_risk": 21,
    "first_engaged": 4,
    "cumulative_engaged_share": 0.48484848484848486
   },
   {
    "round": 14,
    "at_risk": 17,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.5757575757575758
   },
   {
    "round": 15,
    "at_risk": 14,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.6666666666666667
   },
   {
    "round": 16,
    "at_risk": 11,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.7272727272727273
   },
   {
    "round": 17,
    "at_risk": 9,
    "first_engaged": 3,
    "cumulative_engaged_share": 0.8181818181818181
   },
   {
    "round": 18,
    "at_risk": 6,
    "first_engaged": 2,
    "cumulative_engaged_share": 0.8787878787878788
   },
   {
    "round": 19,
    "at_risk": 4,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.9090909090909091
   },
   {
    "round": 20,
    "at_risk": 3,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9090909090909091
   },
   {
    "round": 21,
    "at_risk": 3,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.9090909090909091
   },
   {
    "round": 22,
    "at_risk": 3,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.9393939393939393
   },
   {
    "round": 23,
    "at_risk": 2,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.9696969696969697
   },
   {
    "round": 24,
    "at_risk": 1,
    "first_engaged": 1,
    "cumulative_engaged_share": 1.0
   },
   {
    "round": 25,
    "at_risk": 0,
    "first_engaged": 0,
    "cumulative_engaged_share": 1.0
   },
   {
    "round": 26,
    "at_risk": 0,
    "first_engaged": 0,
    "cumulative_engaged_share": 1.0
   },
   {
    "round": 27,
    "at_risk": 0,
    "first_engaged": 0,
    "cumulative_engaged_share": 1.0
   },
   {
    "round": 28,
    "at_risk": 0,
    "first_engaged": 0,
    "cumulative_engaged_share": 1.0
   },
   {
    "round": 29,
    "at_risk": 0,
    "first_engaged": 0,
    "cumulative_engaged_share": 1.0
   },
   {
    "round": 30,
    "at_risk": 0,
    "first_engaged": 0,
    "cumulative_engaged_share": 1.0
   }
  ]
 }
}
```
