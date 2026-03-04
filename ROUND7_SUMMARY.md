# Round 7 Analysis - Testing the Giants

## Overview
- **Subreddit-rule combinations tested**: 10
- **Comments analyzed**: 1,000
- **Total violations found**: 12 (1.20%)

## Goal
Test the 3 largest subreddits (The_Donald 184K, politics 147K, AskReddit 110K) for all untested rule combinations.

## 🎯 Results Summary

### NEW SOURCES FOUND ≥3%:
1. **askreddit @ advertising** - **4%** ⭐
2. **askreddit @ illegal_activity** - **4%** ⭐

### Overall Performance by Subreddit:
- **AskReddit**: 8/200 violations (4.0%) ✅ BEST
- **politics**: 2/300 violations (0.7%) ❌ LOW
- **The_Donald**: 2/500 violations (0.4%) ❌ VERY LOW

## Detailed Results

### AskReddit (110K comments available) ✅
**Tested**: advertising, illegal_activity
**Total**: 8/200 violations (4.0%)

| Rule | Violations | Rate | Assessment |
|------|------------|------|------------|
| **advertising** | 4/100 | **4%** | ✅ Borderline viable! |
| **illegal_activity** | 4/100 | **4%** | ✅ Borderline viable! |

**Previously tested (Rounds 1-2)**:
- financial_advice (0-1%)
- medical_advice (0-1%)
- legal_advice (0-1%)

**Key Insight**: AskReddit is a general Q&A subreddit where:
- Advertising violations: Promotional links, referral spam
- Illegal activity violations: Drug advice, theft stories, criminal tips

### politics (147K comments available) ❌
**Tested**: medical_advice, financial_advice, legal_advice
**Total**: 2/300 violations (0.7%)

| Rule | Violations | Rate | Assessment |
|------|------------|------|------------|
| legal_advice | 2/100 | 2% | ❌ Too low |
| financial_advice | 0/100 | 0% | ❌ Failed |
| medical_advice | 0/100 | 0% | ❌ Failed |

**Previously tested (Round 3-4)**:
- illegal_activity (2%)
- advertising (3%)

**Key Insight**: Politics is pure political discourse - people debate policy but don't give personal advice.

### The_Donald (184K comments available) ❌
**Tested**: advertising, illegal_activity, medical_advice, financial_advice, legal_advice
**Total**: 2/500 violations (0.4%)

| Rule | Violations | Rate | Assessment |
|------|------------|------|------------|
| advertising | 1/100 | 1% | ❌ Too low |
| legal_advice | 1/100 | 1% | ❌ Too low |
| financial_advice | 0/100 | 0% | ❌ Failed |
| illegal_activity | 0/100 | 0% | ❌ Failed |
| medical_advice | 0/100 | 0% | ❌ Failed |

**Key Insight**: The_Donald is political rallying/memes - surprisingly clean on rule violations despite inflammatory content.

## What Worked ✅

**AskReddit (4% each)**:
1. **advertising (4%)** - Users share referral links, promotional content in answers
2. **illegal_activity (4%)** - Drug discussions, theft stories, criminal tips

## What DIDN'T Work ❌

### The_Donald (0.4% overall):
- Despite 184K comments (largest dataset), violation rate is VERY LOW
- Political rhetoric ≠ rule violations
- Offensive content doesn't necessarily violate our specific rules

### politics (0.7% overall):
- Similar to The_Donald - political debate doesn't produce personal advice
- Policy discussion ≠ actionable recommendations

## Why Round 7 Underperformed (1.20% overall)

### The Paradox: Size ≠ Violations

**The_Donald (184K comments)**:
- Largest subreddit tested
- 0.4% violation rate (lowest of the three)
- **Why**: Political rallying, memes, campaign support
- Content is inflammatory but doesn't violate our specific rules

**politics (147K comments)**:
- Second largest tested
- 0.7% violation rate
- **Why**: Policy debates, not personal situations
- People argue about laws/healthcare/economy but don't give individual advice

**AskReddit (110K comments)**:
- Third largest tested
- 4.0% violation rate (10x better than The_Donald!)
- **Why**: Personal Q&A format
- People share life experiences including rule violations

### Key Lesson:
**Subreddit PURPOSE matters more than SIZE**
- Q&A subreddits (AskReddit) have violations
- Political rallying subreddits (The_Donald) don't
- General advice subreddits (relationships, personalfinance) have violations
- Debate/news subreddits (politics, worldnews) don't

## Updated Best Sources by Rule

### Advertising (now 17 sources ≥3%):
1. videos (16%)
2. pics (11%)
3. food (7%)
4. pcmasterrace (6%)
5. gaming (6%)
6. gonewild (5%)
7. pokemongo (5%)
8. **askreddit (4%)** ⭐ NEW
9. funny (4%)
10. food (4%)
11. politics (3%)
12. diy (3%)
13-17. Various 3% sources

### Illegal Activity (now 6 sources ≥3%):
1. incels (12%)
2. suicidewatch (10%)
3. news (5%)
4. worldnews (5%)
5. **askreddit (4%)** ⭐ NEW
6. conspiracy (4%)
7. europe (4%)
8. mma (4%)

### Financial Advice (still only 1 strong source):
1. personalfinance (13%)
2. relationships (4%)
3. diy (3%)
4. Everything else ≤1%

### Legal Advice (still very limited):
1. purplepilldebate (4%)
2. relationships (3%)
3. politics (2%) ⭐ NEW
4. Everything else ≤2%

### Medical Advice (unchanged):
1. suicidewatch (7%)
2. depression (6%)
3. science (4%)
4. askscience (3%)

## Cumulative Progress

### All Rounds Combined:
- **Round 1**: 25 combinations, 2,500 comments, 220 violations (8.8%)
- **Round 1.5**: 7 combinations, 700 comments, 24 violations (3.43%)
- **Round 2**: 14 combinations, 1,400 comments, 35 violations (2.5%)
- **Round 3**: 15 combinations, 1,500 comments, 45 violations (3.0%)
- **Round 4**: 15 combinations, 1,500 comments, 59 violations (3.93%)
- **Round 5**: 17 combinations, 1,700 comments, 19 violations (1.12%)
- **Round 6**: 16 combinations, 1,600 comments, 13 violations (0.81%)
- **Round 7**: 10 combinations, 1,000 comments, 12 violations (1.20%)

### **GRAND TOTAL**:
- **112 subreddit-rule combinations tested**
- **11,200 comments analyzed**
- **403 violations found**
- **Overall rate: 3.60%**

## New Sources Added

### ≥3% (Borderline Viable):
- **askreddit @ advertising** - 4% ⭐
- **askreddit @ illegal_activity** - 4% ⭐

### 1-2% (Too Low):
- politics @ legal_advice - 2%
- the_donald @ advertising - 1%
- the_donald @ legal_advice - 1%

### 0% (Failed):
- the_donald @ financial_advice, illegal_activity, medical_advice
- politics @ financial_advice, medical_advice

## Files Generated
- `round7_summary.csv` - Full results
- `round7_samples/` - Sample files (10 files)
- `round7_results/` - Analysis results (10 files)
- `ROUND7_SUMMARY.md` - This file

## Key Insights

### Size Doesn't Matter, Purpose Does:
1. **The_Donald (184K) → 0.4%**: Political rallying doesn't violate our rules
2. **politics (147K) → 0.7%**: Policy debates don't contain personal advice
3. **AskReddit (110K) → 4.0%**: Q&A format naturally produces violations

### Best Subreddit Types for Violations:
✅ **Q&A/Advice**: AskReddit, relationships, personalfinance
✅ **Content Sharing**: videos, pics, food, gaming
✅ **Support/Crisis**: suicidewatch, depression
✅ **Debate (specific types)**: purplepilldebate

❌ **Political News/Rallying**: The_Donald, politics, EnoughTrumpSpam
❌ **General Discussion**: philosophy, space, history
❌ **Academic**: AskHistorians, askscience (low rates)

## Recommendations

### High Priority - Test Remaining Q&A Subreddits:
Since AskReddit performed well (4% both rules), we should test similar formats.

Unfortunately, your dataset has limited Q&A subreddits. Already tested:
- AskReddit ✅
- relationships ✅
- AskWomen ✅
- AskHistorians ✅

### Medium Priority - Extract Full Datasets:
We now have **18+ sources ≥3%** across all rules. Time to extract full violation datasets from proven sources.

### Low Priority - Continue Sampling:
Diminishing returns. We've tested 112 combinations, found the patterns. Most remaining subreddits are niche/low-value.
