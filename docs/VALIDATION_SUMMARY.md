# WISE Hypothesis Validation Results

## Overview
- **Total hypotheses tested:** 25
- **Total comments analyzed:** 2,500
- **Total violations found:** 220 (8.8% overall)

## Key Findings

### 🔥 Highest Violation Rates
1. **illegal_activity @ soccerstreams** - 94% (PRIMARY)
2. **spoilers @ anime** - 18% (HIGH)
3. **illegal_activity @ jailbreak** - 15% (PRIMARY)
4. **spoilers @ asoiaf** - 14% (PRIMARY)
5. **financial_advice @ personalfinance** - 13% (PRIMARY)

### ❄️ Lowest Violation Rates (0%)
- medical_advice @ askreddit (HIGH)
- financial_advice @ churning (HIGH)
- medical_advice @ lifeprotips (MEDIUM)
- medical_advice @ askwomen (MEDIUM)
- spoilers @ nosleep (LOW)

## Summary by Rule Type

### Financial Advice
- **Total violations:** 19/500 (3.8%)
- **Best subreddit:** personalfinance (13%)
- **Assessment:** Low violation rate overall; personalfinance shows promise

### Illegal Activity
- **Total violations:** 125/400 (31.25%)
- **Best subreddit:** soccerstreams (94%)
- **Assessment:** VERY HIGH success rate, especially soccerstreams (banned subreddit dedicated to piracy)

### Medical Advice
- **Total violations:** 22/900 (2.4%)
- **Best subreddit:** suicidewatch (7%)
- **Assessment:** Very low violation rates across all subreddits

### Spoilers
- **Total violations:** 54/700 (7.7%)
- **Best subreddit:** anime (18%)
- **Assessment:** Moderate rates; anime, gameofthrones, and asoiaf show decent violation rates

## Hypothesis Accuracy

The wise file predictions were largely **overestimated**:
- Only **1/25 hypotheses (4%)** met their expected confidence thresholds
- PRIMARY priority: 1/10 validated (10%)
- HIGH priority: 0/6 validated (0%)
- MEDIUM priority: 0/8 validated (0%)
- LOW priority: 0/1 validated (0%)

## Recommendations for Production

### HIGH PRIORITY - Worth pursuing:
1. **illegal_activity @ soccerstreams** (94%) - Extremely high accuracy
2. **spoilers @ anime** (18%) - Good signal
3. **illegal_activity @ jailbreak** (15%) - Good signal
4. **spoilers @ asoiaf** (14%) - Good signal
5. **financial_advice @ personalfinance** (13%) - Good signal

### MEDIUM PRIORITY - Consider with caution:
- illegal_activity @ incels (12%)
- spoilers @ gameofthrones (11%)
- medical_advice @ suicidewatch (7%)
- medical_advice @ depression (6%)
- spoilers @ television/movies (4%)

### LOW PRIORITY - Not worth pursuing:
- Most medical_advice combinations (too low signal)
- financial_advice @ churning (0%)
- spoilers @ nosleep (0% - wrong context)

## Next Steps

1. **Focus on illegal_activity detection** - Shows highest violation rates
2. **Refine spoilers detection** - Moderate success in entertainment subreddits
3. **Reconsider medical_advice strategy** - Very low signal, may need different approach
4. **Test financial_advice only on personalfinance** - Other subreddits show minimal violations

## Files Generated
- `wise_validation_summary.csv` - Full detailed results
- `samples/` - All sampled comments (25 files)
- `results/` - Individual analysis results (25 files)
