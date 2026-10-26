# Study 1R results [pipeline test, not results]

**PIPELINE TEST, NOT RESULTS.** Dry run of the analysis pipeline on 10 pilot episodes with pseudo screener and verbal labels from the rule-based detector. No number below is a result.

Episodes: 10; arms: 4.1-high/offer, 4.1-low/offer, mini-low/offer, mini-low/sham.

Errors: 0. Skipped (arms absent): 3.

## T1 primary (mini-low Offer minus Anchor, change score) [pipeline test, not results]

```json
{
 "skipped": "no data for ('mini-low', 'anchor')"
}
```

## T1 secondary, Holm family of five (permutation p) [pipeline test, not results]

```json
{
 "mini-low Offer minus Sham": {
  "estimate": 0.3680000000000021,
  "ci_low": -0.1252500000000083,
  "ci_high": 0.8612500000000125,
  "level": 0.95,
  "p_bootstrap": 0.374,
  "n_a": 2,
  "n_b": 2,
  "excludes_zero": false,
  "p_permutation": 0.6643335666433356,
  "p_holm": 0.6643335666433356
 },
 "mini-low Anchor minus Sham": {
  "skipped": "no data for ('mini-low', 'anchor')"
 },
 "mini-low Sham minus Silent": {
  "skipped": "no data for ('mini-low', 'silent')"
 },
 "4.1-low Offer minus Anchor (secondary T1)": {
  "skipped": "no data for ('4.1-low', 'anchor')"
 },
 "4.1-high Offer minus Silent (disruption)": {
  "skipped": "no data for ('4.1-high', 'silent')"
 }
}
```

## Disruption in mini-low and 4.1-low (descriptive) [pipeline test, not results]

```json
{
 "mini-low Offer minus Silent (disruption, descriptive)": {
  "skipped": "no data for ('mini-low', 'silent')"
 },
 "4.1-low Offer minus Silent (disruption, descriptive)": {
  "skipped": "no data for ('4.1-low', 'silent')"
 }
}
```

## T1 secondary, ANCOVA (uncorrected) [pipeline test, not results]

```json
{
 "skipped": "needs mini-low Offer and Anchor"
}
```

## T1 secondary, Fisher on the behavioral flag (uncorrected) [pipeline test, not results]

```json
{
 "skipped": "needs mini-low Offer and Anchor"
}
```

## T2a primary (inclusive, rounds 11-30) [pipeline test, not results]

```json
{
 "estimate": 0.3333333333333333,
 "ci_low": 0.0,
 "ci_high": 1.0,
 "level": 0.95,
 "p_bootstrap": 0.5744,
 "n_a": 3,
 "n_b": 3,
 "excludes_zero": false,
 "measure": "acc_inclusive",
 "verdict": "not supported"
}
```

## T2a secondary (strict; lower bound under the stopping rule) [pipeline test, not results]

```json
{
 "estimate": 0.3333333333333333,
 "ci_low": 0.0,
 "ci_high": 1.0,
 "level": 0.95,
 "p_bootstrap": 0.5744,
 "n_a": 3,
 "n_b": 3,
 "excludes_zero": false,
 "measure": "acc_strict",
 "verdict": "not supported"
}
```

## T2a sensitivity (inclusive, rounds 11-12; lower bound under the stopping rule) [pipeline test, not results]

```json
{
 "estimate": 0.0,
 "ci_low": 0.0,
 "ci_high": 0.0,
 "level": 0.95,
 "p_bootstrap": 1.0,
 "n_a": 3,
 "n_b": 3,
 "excludes_zero": false,
 "measure": "acc_inclusive_11_12",
 "verdict": "not supported"
}
```

## T2a sensitivity, corrected for the estimated miss rate [pipeline test, not results]

```json
{
 "estimate": 0.3333333333333333,
 "ci_low": 0.0,
 "ci_high": 1.0,
 "excludes_zero": false,
 "rate_high": 0.3333333333333333,
 "rate_low": 0.0,
 "n_high": 3,
 "n_low": 3,
 "p_audit_flagged": 0.0,
 "p_audit_unflagged": 0.0,
 "measure": "inclusive acceptance corrected for the estimated miss rate",
 "verdict": "not supported"
}
```

## Miss audit (option A; secondary) [pipeline test, not results]

```json
{
 "strata": {
  "audit_flagged": {
   "audited": 6,
   "accepted": 0,
   "rate": 0.0,
   "ci": [
    2.7755575615628914e-17,
    0.3903342879021653
   ],
   "screener_negatives": 58,
   "uncoded": 52
  },
  "audit_unflagged": {
   "audited": 50,
   "accepted": 0,
   "rate": 0.0,
   "ci": [
    6.938893903907228e-18,
    0.07134759913335872
   ],
   "screener_negatives": 181,
   "uncoded": 131
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
  "messages": 1,
  "uncoded": 0,
  "coded": 1,
  "accepting_episodes": 1
 },
 "audit_accepting_episodes_not_in_primary": 0
}
```

## T2a secondary, logistic regression on cell and jump [pipeline test, not results]

```json
{
 "n": 6,
 "converged": false,
 "separation_suspected": true,
 "coefficients": {
  "intercept": {
   "estimate": 1575.949055343593,
   "se": 6165437.5454054605,
   "ci_low": -12082459.588870393,
   "ci_high": 12085611.48698108
  },
  "cell_4.1-high": {
   "estimate": -1269.1218530155195,
   "se": 5118125.02758527,
   "ci_low": -10032609.844293216,
   "ci_high": 10030071.600587184
  },
  "jump": {
   "estimate": -222.73681722036554,
   "se": 746984.5582186506,
   "ci_low": -1464285.567933339,
   "ci_high": 1463840.094298898
  }
 }
}
```

## T2a sensitivity, alternative coding (inclusive) [pipeline test, not results]

```json
{
 "estimate": 0.3333333333333333,
 "ci_low": 0.0,
 "ci_high": 1.0,
 "level": 0.95,
 "p_bootstrap": 0.5744,
 "n_a": 3,
 "n_b": 3,
 "excludes_zero": false,
 "measure": "acc_inclusive_alt",
 "verdict": "not supported"
}
```

## T2a sensitivity, alternative coding (strict; lower bound) [pipeline test, not results]

```json
{
 "estimate": 0.3333333333333333,
 "ci_low": 0.0,
 "ci_high": 1.0,
 "level": 0.95,
 "p_bootstrap": 0.5744,
 "n_a": 3,
 "n_b": 3,
 "excludes_zero": false,
 "measure": "acc_strict_alt",
 "verdict": "not supported"
}
```

## Alternative coding: reclassified messages (sensitivity) [pipeline test, not results]

```json
{
 "4.1-low": {
  "episodes": 3,
  "reclassified_messages": 12
 },
 "4.1-high": {
  "episodes": 3,
  "reclassified_messages": 3
 }
}
```

## T2b per cell (secondary) [pipeline test, not results]

```json
{
 "mini-low": {
  "skipped": "needs Offer and Silent in mini-low"
 },
 "4.1-low": {
  "skipped": "needs Offer and Silent in 4.1-low"
 },
 "4.1-high": {
  "skipped": "needs Offer and Silent in 4.1-high"
 }
}
```

## Compliance table (secondary) [pipeline test, not results]

```json
{
 "mini-low": {
  "skipped": "no Offer episodes with verbal labels in mini-low"
 },
 "4.1-low": {
  "table": {
   "V+B+": 0,
   "V+B-": 0,
   "V-B+": 0,
   "V-B-": 3
  },
  "n": 3,
  "accepts_without_behavioral_movement": null,
  "ci_low": null,
  "ci_high": null
 },
 "4.1-high": {
  "table": {
   "V+B+": 0,
   "V+B-": 1,
   "V-B+": 0,
   "V-B-": 2
  },
  "n": 3,
  "accepts_without_behavioral_movement": 1.0,
  "ci_low": 0.20654931437723745,
  "ci_high": 1.0
 }
}
```

## Calibration table (secondary) [pipeline test, not results]

```json
{
 "mini-low": {
  "silent_n": 0,
  "offer_n": 2,
  "propensity_91.80": null,
  "propensity_92.70": null,
  "propensity_94.50": null,
  "silent_mean_post": null,
  "offer_acc_inclusive": null,
  "offer_behavioral_acceptance": 0.0
 },
 "4.1-low": {
  "silent_n": 0,
  "offer_n": 3,
  "propensity_91.80": null,
  "propensity_92.70": null,
  "propensity_94.50": null,
  "silent_mean_post": null,
  "offer_acc_inclusive": 0.0,
  "offer_behavioral_acceptance": 0.0
 },
 "4.1-high": {
  "silent_n": 0,
  "offer_n": 3,
  "propensity_91.80": null,
  "propensity_92.70": null,
  "propensity_94.50": null,
  "silent_mean_post": null,
  "offer_acc_inclusive": 0.3333333333333333,
  "offer_behavioral_acceptance": 0.0
 }
}
```

## Awareness probe (secondary; aware acceptance a lower bound under the stopping rule) [pipeline test, not results]

```json
{
 "per_arm": {},
 "offer_minus_silent": {},
 "aware_acceptance": {}
}
```

## Round of first engagement (descriptive; detector- and screener-based) [pipeline test, not results]

```json
{
 "mini-low (detector)": {
  "basis": "detector",
  "curve": [
   {
    "round": 11,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 12,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 13,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 14,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 15,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 16,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 17,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 18,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 19,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 20,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 21,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 22,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 23,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 24,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 25,
    "at_risk": 2,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 26,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 27,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 28,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 29,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 30,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5
   }
  ]
 },
 "mini-low (judge v2 screener)": {
  "basis": "judge v2 screener",
  "curve": [
   {
    "round": 11,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 12,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 13,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 14,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 15,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 16,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 17,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 18,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 19,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 20,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 21,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 22,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 23,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 24,
    "at_risk": 2,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.0
   },
   {
    "round": 25,
    "at_risk": 2,
    "first_engaged": 1,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 26,
    "at_risk": 1,
    "first_engaged": 0,
    "cumulative_engaged_share": 0.5
   },
   {
    "round": 27,
    "at_ris
```

## Exploratory (test suspicion, acceptance by round as a lower bound, ACK rates) [pipeline test, not results]

```json
{
 "public_private_gap": {},
 "test_suspicion": {
  "4.1-high/offer": 0.0,
  "4.1-low/offer": 0.0
 },
 "ack_rate": {
  "4.1-high/offer": 0.5087719298245614,
  "4.1-low/offer": 0.5175438596491229,
  "mini-low/offer": 0.17105263157894735,
  "mini-low/sham": 0.013157894736842105
 },
 "acceptance_by_round": {
  "4.1-low": {
   "11": 0.0,
   "12": 0.0,
   "13": 0.0,
   "14": 0.0,
   "15": 0.0,
   "16": 0.0,
   "17": 0.0,
   "18": 0.0,
   "19": 0.0,
   "20": 0.0,
   "21": 0.0,
   "22": 0.0,
   "23": 0.0,
   "24": 0.0,
   "25": 0.0,
   "26": 0.0,
   "27": 0.0,
   "28": 0.0,
   "29": 0.0,
   "30": 0.0
  },
  "4.1-high": {
   "11": 0.0,
   "12": 0.0,
   "13": 0.0,
   "14": 0.0,
   "15": 0.0,
   "16": 0.0,
   "17": 0.0,
   "18": 0.0,
   "19": 0.0,
   "20": 0.3333333333333333,
   "21": 0.0,
   "22": 0.0,
   "23": 0.0,
   "24": 0.0,
   "25": 0.0,
   "26": 0.0,
   "27": 0.0,
   "28": 0.0,
   "29": 0.0,
   "30": 0.0
  }
 }
}
```

## Pre-enumerated outcomes (descriptive) [pipeline test, not results]

```json
{
 "compression": {
  "t2a": {
   "estimate": 0.3333333333333333,
   "ci_low": 0.0,
   "ci_high": 1.0,
   "level": 0.95,
   "p_bootstrap": 0.5744,
   "n_a": 3,
   "n_b": 3,
   "excludes_zero": false,
   "measure": "acc_inclusive",
   "verdict": "not supported"
  },
  "propensity_difference_silent": {
   "skipped": "needs Silent in 4.1-high and 4.1-low"
  },
  "compression": null
 },
 "anchoring_dominance": {
  "skipped": "needs mini-low Offer, Anchor and Sham"
 },
 "says_yes_does_not_act": {
  "mini-low": {
   "skipped": "no Offer episodes with verbal labels in mini-low"
  },
  "4.1-low": {
   "table": {
    "V+B+": 0,
    "V+B-": 0,
    "V-B+": 0,
    "V-B-": 3
   },
   "n": 3,
   "accepts_without_behavioral_movement": null,
   "ci_low": null,
   "ci_high": null
  },
  "4.1-high": {
   "table": {
    "V+B+": 0,
    "V+B-": 1,
    "V-B+": 0,
    "V-B-": 2
   },
   "n": 3,
   "accepts_without_behavioral_movement": 1.0,
   "ci_low": 0.20654931437723745,
   "ci_high": 1.0
  }
 },
 "ignoring": {
  "mini-low (judge v2 screener)": {
   "n": 2,
   "never_engaged": 1,
   "share": 0.5,
   "ci": [
    0.09453120573423074,
    0.9054687942657693
   ]
  },
  "mini-low (detector)": {
   "n": 2,
   "never_engaged": 1,
   "share": 0.5,
   "ci": [
    0.09453120573423074,
    0.9054687942657693
   ]
  },
  "4.1-low (judge v2 screener)": {
   "n": 3,
   "never_engaged": 1,
   "share": 0.3333333333333333,
   "ci": [
    0.06149194472039621,
    0.7923403991979522
   ]
  },
  "4.1-low (detector)": {
   "n": 3,
   "never_engaged": 1,
   "share": 0.3333333333333333,
   "ci": [
    0.06149194472039621,
    0.7923403991979522
   ]
  },
  "4.1-high (judge v2 screener)": {
   "n": 3,
   "never_engaged": 0,
   "share": 0.0,
   "ci": [
    5.551115123125783e-17,
    0.5614970317550454
   ]
  },
  "4.1-high (detector)": {
   "n": 3,
   "never_engaged": 0,
   "share": 0.0,
   "ci": [
    5.551115123125783e-17,
    0.5614970317550454
   ]
  }
 }
}
```

## Judge comparison figure (exploratory: v1-read, v2-read, human-confirmed, behavioral) [pipeline test, not results]

```json
{
 "mini-low": {
  "v1_read": {
   "k": 0,
   "n": 0,
   "rate": null,
   "ci": null
  },
  "v2_read": {
   "k": 0,
   "n": 2,
   "rate": 0.0,
   "ci": [
    0.0,
    0.6576197724933469
   ]
  },
  "human_coded": {
   "k": 0,
   "n": 0,
   "rate": null,
   "ci": null
  },
  "behavioral_flag": {
   "k": 0,
   "n": 2,
   "rate": 0.0,
   "ci": [
    0.0,
    0.6576197724933469
   ]
  }
 },
 "4.1-low": {
  "v1_read": {
   "k": 0,
   "n": 0,
   "rate": null,
   "ci": null
  },
  "v2_read": {
   "k": 0,
   "n": 3,
   "rate": 0.0,
   "ci": [
    5.551115123125783e-17,
    0.5614970317550454
   ]
  },
  "human_coded": {
   "k": 0,
   "n": 3,
   "rate": 0.0,
   "ci": [
    5.551115123125783e-17,
    0.5614970317550454
   ]
  },
  "behavioral_flag": {
   "k": 0,
   "n": 3,
   "rate": 0.0,
   "ci": [
    5.551115123125783e-17,
    0.5614970317550454
   ]
  }
 },
 "4.1-high": {
  "v1_read": {
   "k": 0,
   "n": 0,
   "rate": null,
   "ci": null
  },
  "v2_read": {
   "k": 1,
   "n": 3,
   "rate": 0.3333333333333333,
   "ci": [
    0.06149194472039621,
    0.7923403991979522
   ]
  },
  "human_coded": {
   "k": 1,
   "n": 3,
   "rate": 0.3333333333333333,
   "ci": [
    0.06149194472039621,
    0.7923403991979522
   ]
  },
  "behavioral_flag": {
   "k": 0,
   "n": 3,
   "rate": 0.0,
   "ci": [
    5.551115123125783e-17,
    0.5614970317550454
   ]
  }
 }
}
```

## Study 1R-A add-on (preregistered; run only on the entrant's approval) [pipeline test, not results]

```json
{
 "disruption": {
  "skipped": "no data for ('4.1-high', 'competitive')"
 },
 "propensity": {}
}
```

## Skipped [pipeline test, not results]

- T1 primary (mini-low Offer minus Anchor, change score): no data for ('mini-low', 'anchor')
- T1 secondary, ANCOVA (uncorrected): needs mini-low Offer and Anchor
- T1 secondary, Fisher on the behavioral flag (uncorrected): needs mini-low Offer and Anchor
