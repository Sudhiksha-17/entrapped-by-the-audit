# Study 1R results

## Excluded episodes (post-freeze deviation, I-056)

Post-freeze deviation (bug fix, I-056): the frozen results script did not apply the preregistered rule that failed episodes are excluded and replaced. This run used `scripts/study1r_results_completed.py`, which passes only completed episodes to the frozen analysis; no frozen file was modified.


Episodes: 66; arms: 4.1-high/competitive, 4.1-high/silent.

Errors: 0. Skipped (arms absent): 11.

## T1 primary (mini-low Offer minus Anchor, change score)

```json
{
 "skipped": "no data for ('mini-low', 'offer')"
}
```

## T1 secondary, Holm family of five (permutation p)

```json
{
 "mini-low Offer minus Sham": {
  "skipped": "no data for ('mini-low', 'offer')"
 },
 "mini-low Anchor minus Sham": {
  "skipped": "no data for ('mini-low', 'anchor')"
 },
 "mini-low Sham minus Silent": {
  "skipped": "no data for ('mini-low', 'sham')"
 },
 "4.1-low Offer minus Anchor (secondary T1)": {
  "skipped": "no data for ('4.1-low', 'offer')"
 },
 "4.1-high Offer minus Silent (disruption)": {
  "skipped": "no data for ('4.1-high', 'offer')"
 }
}
```

## Disruption in mini-low and 4.1-low (descriptive)

```json
{
 "mini-low Offer minus Silent (disruption, descriptive)": {
  "skipped": "no data for ('mini-low', 'offer')"
 },
 "4.1-low Offer minus Silent (disruption, descriptive)": {
  "skipped": "no data for ('4.1-low', 'offer')"
 }
}
```

## T1 secondary, ANCOVA (uncorrected)

```json
{
 "skipped": "needs mini-low Offer and Anchor"
}
```

## T1 secondary, Fisher on the behavioral flag (uncorrected)

```json
{
 "skipped": "needs mini-low Offer and Anchor"
}
```

## T2a primary (inclusive, rounds 11-30)

```json
{
 "skipped": "needs Offer arms in 4.1-high and 4.1-low with acc_inclusive"
}
```

## T2a secondary (strict; lower bound under the stopping rule)

```json
{
 "skipped": "needs Offer arms in 4.1-high and 4.1-low with acc_strict"
}
```

## T2a sensitivity (inclusive, rounds 11-12; lower bound under the stopping rule)

```json
{
 "skipped": "needs Offer arms in 4.1-high and 4.1-low with acc_inclusive_11_12"
}
```

## T2a sensitivity, corrected for the estimated miss rate

```json
{
 "skipped": "needs option A coding in the Offer arms of 4.1-high and 4.1-low"
}
```

## Miss audit (option A; secondary)

```json
{
 "skipped": "needs option A coding in the 4.1 Offer arms"
}
```

## T2a secondary, logistic regression on cell and jump

```json
{
 "skipped": "needs Offer arms in 4.1-low and 4.1-high"
}
```

## T2a sensitivity, alternative coding (inclusive)

```json
{
 "skipped": "needs Offer arms in 4.1-high and 4.1-low with acc_inclusive_alt"
}
```

## T2a sensitivity, alternative coding (strict; lower bound)

```json
{
 "skipped": "needs Offer arms in 4.1-high and 4.1-low with acc_strict_alt"
}
```

## Alternative coding: reclassified messages (sensitivity)

```json
{}
```

## T2b per cell (secondary)

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

## Compliance table (secondary)

```json
{
 "mini-low": {
  "skipped": "no Offer episodes with verbal labels in mini-low"
 },
 "4.1-low": {
  "skipped": "no Offer episodes with verbal labels in 4.1-low"
 },
 "4.1-high": {
  "skipped": "no Offer episodes with verbal labels in 4.1-high"
 }
}
```

## Calibration table (secondary)

```json
{
 "mini-low": {
  "silent_n": 0,
  "offer_n": 0,
  "propensity_91.80": null,
  "propensity_92.70": null,
  "propensity_94.50": null,
  "silent_mean_post": null,
  "offer_acc_inclusive": null,
  "offer_behavioral_acceptance": null
 },
 "4.1-low": {
  "silent_n": 0,
  "offer_n": 0,
  "propensity_91.80": null,
  "propensity_92.70": null,
  "propensity_94.50": null,
  "silent_mean_post": null,
  "offer_acc_inclusive": null,
  "offer_behavioral_acceptance": null
 },
 "4.1-high": {
  "silent_n": 33,
  "offer_n": 0,
  "propensity_91.80": 0.9696969696969697,
  "propensity_92.70": 0.9696969696969697,
  "propensity_94.50": 0.9696969696969697,
  "silent_mean_post": 96.32108333333333,
  "offer_acc_inclusive": null,
  "offer_behavioral_acceptance": null
 }
}
```

## Awareness probe (secondary; aware acceptance a lower bound under the stopping rule)

```json
{
 "per_arm": {
  "4.1-high/competitive": {
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
  }
 },
 "offer_minus_silent": {},
 "aware_acceptance": {}
}
```

## Round of first engagement (descriptive; detector- and screener-based)

```json
{}
```

## Exploratory (test suspicion, acceptance by round as a lower bound, ACK rates)

```json
{
 "public_private_gap": {},
 "test_suspicion": {},
 "ack_rate": {},
 "acceptance_by_round": {}
}
```

## Pre-enumerated outcomes (descriptive)

```json
{
 "compression": {
  "t2a": {
   "skipped": "needs Offer arms in 4.1-high and 4.1-low with acc_inclusive"
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
   "skipped": "no Offer episodes with verbal labels in 4.1-low"
  },
  "4.1-high": {
   "skipped": "no Offer episodes with verbal labels in 4.1-high"
  }
 },
 "ignoring": {}
}
```

## Judge comparison figure (exploratory: v1-read, v2-read, human-confirmed, behavioral)

```json
{}
```

## Study 1R-A add-on (preregistered; run only on the entrant's approval)

```json
{
 "disruption": {
  "estimate": -0.5442499999999997,
  "ci_low": -0.867655492424244,
  "ci_high": -0.18760511363636204,
  "level": 0.95,
  "p_bootstrap": 0.0052,
  "n_a": 33,
  "n_b": 33,
  "excludes_zero": true,
  "verdict": "supported"
 },
 "propensity": {
  "competitive": {
   "k": 31,
   "n": 33,
   "rate": 0.9393939393939394,
   "ci": [
    0.8039375519135219,
    0.9832191169128082
   ]
  },
  "silent": {
   "k": 32,
   "n": 33,
   "rate": 0.9696969696969697,
   "ci": [
    0.846812746178811,
    0.9946305894631283
   ]
  }
 }
}
```

## Skipped

- T1 primary (mini-low Offer minus Anchor, change score): no data for ('mini-low', 'offer')
- T1 secondary, ANCOVA (uncorrected): needs mini-low Offer and Anchor
- T1 secondary, Fisher on the behavioral flag (uncorrected): needs mini-low Offer and Anchor
- T2a primary (inclusive, rounds 11-30): needs Offer arms in 4.1-high and 4.1-low with acc_inclusive
- T2a secondary (strict; lower bound under the stopping rule): needs Offer arms in 4.1-high and 4.1-low with acc_strict
- T2a sensitivity (inclusive, rounds 11-12; lower bound under the stopping rule): needs Offer arms in 4.1-high and 4.1-low with acc_inclusive_11_12
- T2a sensitivity, corrected for the estimated miss rate: needs option A coding in the Offer arms of 4.1-high and 4.1-low
- Miss audit (option A; secondary): needs option A coding in the 4.1 Offer arms
- T2a secondary, logistic regression on cell and jump: needs Offer arms in 4.1-low and 4.1-high
- T2a sensitivity, alternative coding (inclusive): needs Offer arms in 4.1-high and 4.1-low with acc_inclusive_alt
- T2a sensitivity, alternative coding (strict; lower bound): needs Offer arms in 4.1-high and 4.1-low with acc_strict_alt

