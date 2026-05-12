# Round 6 Analysis - Financial & Legal Advice Deep Dive

## Overview
- **Subreddit-rule combinations tested**: 16
- **Comments analyzed**: 1,600
- **Total violations found**: 13 (0.81%)

## Goal
Push harder for financial_advice and legal_advice violations by testing career/advice-oriented and political/legal subreddits.

## Results Summary

### 🎯 ONE NEW SOURCE FOUND ≥3%:
- **purplepilldebate @ legal_advice** - **4%** ⭐

### Overall Performance:
- **financial_advice**: 3/800 violations (0.4%) ❌ VERY LOW
- **legal_advice**: 10/800 violations (1.2%) ❌ LOW

## Detailed Results

### Financial Advice 💰
**Total**: 3/800 violations (0.4%)

| Subreddit | Violations | Rate | Assessment |
|-----------|------------|------|------------|
| askhistorians | 1/100 | 1% | ❌ Too low (academic career advice) |
| lifeprotips | 1/100 | 1% | ❌ Too low (debt repayment tip) |
| tifu | 1/100 | 1% | ❌ Too low ("get a job" comment) |
| getmotivated | 0/100 | 0% | ❌ Failed |
| iama | 0/100 | 0% | ❌ Failed |
| philosophy | 0/100 | 0% | ❌ Failed |
| space | 0/100 | 0% | ❌ Failed |
| technology | 0/100 | 0% | ❌ Failed |

**Key Insight**: Even advice/career-focused subreddits do NOT provide financial advice at meaningful rates. People systematically avoid giving specific investment/tax/retirement/career recommendations.

### Legal Advice ⚖️
**Total**: 10/800 violations (1.2%)

| Subreddit | Violations | Rate | Assessment |
|-----------|------------|------|------------|
| **purplepilldebate** | 4/100 | **4%** | ✅ Borderline! (1st Amendment misinterpretations, legal defenses) |
| shitredditsays | 2/100 | 2% | ⚠️ Low (Stand Your Ground law discussion) |
| askhistorians | 1/100 | 1% | ❌ Too low (historical legal interpretation) |
| enoughtrumpspam | 1/100 | 1% | ❌ Too low (campaign finance interpretation) |
| europe | 1/100 | 1% | ❌ Too low (treason question) |
| neutralpolitics | 1/100 | 1% | ❌ Too low (FRCP Rule 37 interpretation) |
| canadapolitics | 0/100 | 0% | ❌ Failed |
| history | 0/100 | 0% | ❌ Failed |

**Key Insight**: Legal advice is slightly more common than financial advice (1.2% vs 0.4%), but still very rare. People discuss laws but avoid offering actionable legal guidance.

## What Worked ✅

1. **purplepilldebate @ legal_advice (4%)** - Gender debate subreddit with:
   - First Amendment misinterpretations (claiming moderation violates free speech)
   - Legal defenses discussion (freeze response in assault cases)
   - This is our FIRST legal_advice source ≥4%!

## What DIDN'T Work ❌

### Career/Advice Subreddits for Financial Advice:
- **iama** (0%) - Even career AMAs don't give specific career advice
- **getmotivated** (0%) - Motivational, not financial
- **lifeprotips** (1%) - Only 1 debt repayment comment
- **tifu** (1%) - Only 1 "get a job" insult
- **technology** (0%) - Tech discussions, not career advice

### Political/Legal Subreddits for Legal Advice:
- Most political subs (0-1%) - People discuss law, but don't offer legal advice
- **neutralpolitics** (1%) - Even evidence-based policy discussions rarely give legal advice
- **canadapolitics** (0%) - Pure political discourse

### Academic Subreddits:
- **askhistorians** (1% both rules) - Historical discussions, not advice
- **history** (0%) - Same issue
- **space** (0%), **philosophy** (0%) - Not advice forums

## Why Round 6 Underperformed (0.81% overall)

### Core Issue: Reddit Culture Avoids Advice Liability

**Financial Advice (0.4%)**:
- Users systematically avoid specific investment/tax/retirement recommendations
- Even in career-focused subs (IAmA), people share experiences but don't advise
- Legal liability concerns likely drive this behavior

**Legal Advice (1.2%)**:
- People distinguish "discussing law" vs "giving legal advice"
- Even constitutional debates (NeutralPolitics) are opinions, not guidance
- Exception: **purplepilldebate** (4%) has more legal misinterpretations because:
  - Heated gender debates lead to First Amendment claims
  - Self-defense legal arguments in assault discussions
  - Users less careful about legal accuracy

## Updated Best Sources by Rule

### Financial Advice
1. **personalfinance** (13%) - **ONLY strong source**
2. relationships (4%) - Borderline
3. diy (3%) - Borderline
4. Everything else ≤1% - Not viable

**Status**: Severely limited. personalfinance is essentially the only production source.

### Legal Advice
1. **purplepilldebate** (4%) ⭐ NEW - Borderline viable
2. relationships (3%) - Borderline
3. Everything else ≤2% - Too low

**Status**: Still very limited. purplepilldebate is our best new find, but still only borderline.

## Cumulative Progress

### All Rounds Combined:
- **Round 1**: 25 combinations, 2,500 comments, 220 violations (8.8%)
- **Round 1.5**: 7 combinations, 700 comments, 24 violations (3.43%)
- **Round 2**: 14 combinations, 1,400 comments, 35 violations (2.5%)
- **Round 3**: 15 combinations, 1,500 comments, 45 violations (3.0%)
- **Round 4**: 15 combinations, 1,500 comments, 59 violations (3.93%)
- **Round 5**: 17 combinations, 1,700 comments, 19 violations (1.12%)
- **Round 6**: 16 combinations, 1,600 comments, 13 violations (0.81%)

### **GRAND TOTAL**:
- **102 subreddit-rule combinations tested**
- **10,200 comments analyzed**
- **391 violations found**
- **Overall rate: 3.83%**

## New Sources Added

### ≥3% (Production-Ready):
- **purplepilldebate @ legal_advice** - 4% ⭐

### 1-2% (Borderline):
- shitredditsays @ legal_advice - 2%
- All others - 1% or 0%

## Key Lessons Learned

### Financial Advice is EXTREMELY RARE on Reddit:
1. **Only personalfinance (13%) works** at scale
2. Even career/advice subreddits avoid specific recommendations
3. General discussion subs (India, Canada, philosophy) have 0% rates
4. Motivational/self-improvement subs (GetMotivated) are not financial advice

### Legal Advice is RARE but Slightly More Common:
1. **purplepilldebate (4%)** works due to heated debates leading to legal claims
2. Political subs discuss law but don't give advice (0-1%)
3. Drama/conflict subs also very low (0-2%)
4. Academic/historical subs discuss legal history, not advice (0-1%)

### Why These Rules Are Hard to Find:
- **Liability concerns**: Users avoid giving advice that could be legally actionable
- **Community norms**: Most subreddits explicitly ban financial/legal advice
- **Cultural awareness**: Redditors distinguish "discussing" vs "advising"
- **Exception pattern**: Heated debate subreddits (purplepilldebate) have more violations because users make legal claims to win arguments, not provide genuine advice

## Files Generated
- `round6_summary.csv` - Full results
- `round6_samples/` - Sample files (16 files)
- `round6_results/` - Analysis results (16 files)
- `ROUND6_SUMMARY.md` - This file

## Recommendations Going Forward

### For Financial Advice:
**STOP testing general subreddits**. The data is clear:
- personalfinance (13%) is the ONLY strong source
- No other tested subreddit exceeds 4%
- Even specialized advice subs fail (0-1%)

**Accept reality**: Financial advice violations are naturally rare on Reddit.

### For Legal Advice:
**Limited value in continuing**:
- purplepilldebate (4%) is our best new find
- relationships (3%) from earlier rounds
- Everything else ≤2%

**Possible new directions**:
- Test more debate/argument subreddits (similar to purplepilldebate)
- Test men's rights / gender politics subs (likely to have legal claims)
- Test conspiracy subs (might make legal interpretations)

### Overall Strategy:
**Pivot to extraction and other rules**:
1. Extract full datasets from top sources (15 sources ≥6%)
2. Focus on proven categories: advertising, spoilers, illegal_activity, medical_advice
3. Accept that financial/legal advice are rare and move forward with what we have
