# Data Expansion Analysis - Round 2

## Overview
- **Goal**: Find additional subreddits with rule violations to expand training data
- **Subreddits tested**: 14 new subreddit-rule combinations
- **Comments analyzed**: 1,400
- **Total violations found**: 35 (2.5% overall)

## Results by Rule

### 1. Advertising (NEW RULE!)
**Total**: 13/300 violations (4.3%)

| Subreddit | Violations | Rate |
|-----------|------------|------|
| **pcmasterrace** | 6/100 | **6%** ✅ |
| **pokemongo** | 5/100 | **5%** ✅ |
| android | 2/100 | 2% |

**Assessment**: Good sources! pcmasterrace and pokemongo have decent violation rates.

### 2. Financial Advice
**Total**: 3/200 violations (1.5%)

| Subreddit | Violations | Rate |
|-----------|------------|------|
| relationships | 2/100 | 2% |
| askreddit | 1/100 | 1% |

**Assessment**: Low signal. Original personalfinance (13%) is much better.

### 3. Medical Advice
**Total**: 6/300 violations (2.0%)

| Subreddit | Violations | Rate |
|-----------|------------|------|
| **relationships** | 4/100 | **4%** |
| askreddit | 1/100 | 1% |
| twoxchromosomes | 1/100 | 1% |

**Assessment**: relationships (4%) is okay, but depression (6%) and suicidewatch (7%) from original are still better.

### 4. Illegal Activity
**Total**: 2/100 violations (2.0%)

| Subreddit | Violations | Rate |
|-----------|------------|------|
| blackpeopletwitter | 2/100 | 2% |

**Assessment**: Low signal. Original incels (12%) and suicidewatch (10%) are much better.

### 5. Legal Advice (NEW RULE!)
**Total**: 4/200 violations (2.0%)

| Subreddit | Violations | Rate |
|-----------|------------|------|
| **relationships** | 3/100 | **3%** |
| askreddit | 1/100 | 1% |

**Assessment**: relationships (3%) is decent for a new rule category.

### 6. Spoilers
**Total**: 7/300 violations (2.3%)

| Subreddit | Violations | Rate |
|-----------|------------|------|
| **television** | 4/100 | **4%** |
| **movies** | 3/100 | **3%** |
| leagueoflegends | 0/100 | 0% |

**Assessment**: television (4%) and movies (3%) are okay additions, but anime (18%) and gameofthrones (11%) are still best.

## High-Value Discoveries (≥3%)

### Worth Adding to Production:

1. **advertising @ pcmasterrace** - 6%
2. **advertising @ pokemongo** - 5%
3. **medical_advice @ relationships** - 4%
4. **spoilers @ television** - 4%
5. **legal_advice @ relationships** - 3%
6. **spoilers @ movies** - 3%

### New Rules Discovered:

1. **Advertising** - We didn't have good sources before, now we have 2!
2. **Legal Advice** - New rule category with relationships as a decent source

## Updated Production Recommendations

### By Rule (Best Sources):

#### Financial Advice
- **personalfinance** (13%) ⭐ PRIMARY
- lifeprotips (3%)

#### Medical Advice
- **depression** (6%) ⭐ PRIMARY
- **suicidewatch** (7%) ⭐ PRIMARY
- relationships (4%) - NEW addition
- sex (1%)

#### Illegal Activity
- **incels** (12%) ⭐ PRIMARY
- **suicidewatch** (10%) ⭐ PRIMARY
- blackpeopletwitter (2%)

#### Spoilers
- **anime** (18%) ⭐ PRIMARY
- **gameofthrones** (11%) ⭐ PRIMARY
- asoiaf (14%) ⭐ PRIMARY
- television (4%) - NEW addition
- movies (3%) - NEW addition

#### Advertising (NEW!)
- **pcmasterrace** (6%) ⭐ PRIMARY
- **pokemongo** (5%) ⭐ PRIMARY
- android (2%)

#### Legal Advice (NEW!)
- **relationships** (3%) ⭐ PRIMARY
- askreddit (1%)

## Key Insights

### What Worked:
1. **relationships** - Multi-purpose subreddit with violations across medical, financial, and legal advice
2. **pcmasterrace & pokemongo** - Good sources for advertising violations
3. **television & movies** - Decent spoiler sources to supplement the top performers

### What Didn't Work:
1. **askreddit** - Too generic, low signal across all rules (1%)
2. **leagueoflegends** - 0% spoilers (wrong type of content)
3. **blackpeopletwitter** - Only 2% illegal activity (edgy humor ≠ promoting crime)

### Surprises:
1. **Advertising rule** - Found good sources we didn't have before!
2. **Legal advice** - Emerged as a viable new rule category
3. **relationships** - Versatile subreddit hitting multiple rule types

## Overall Statistics

### Original Analysis (Round 1):
- Subreddits tested: 25
- Comments: 2,500
- Violations: 220 (8.8%)

### Expansion (Round 2):
- Subreddits tested: 14
- Comments: 1,400
- Violations: 35 (2.5%)

### Combined Total:
- Subreddits tested: 39
- Comments: 3,900
- Violations: 255 (6.5%)

## Next Steps

1. **Add new sources** to existing rules:
   - spoilers: television, movies
   - medical_advice: relationships

2. **Implement new rules**:
   - advertising: pcmasterrace, pokemongo
   - legal_advice: relationships

3. **Extract training data** from high-value sources (≥3% rate)

4. **Consider skipping** low-signal subreddits:
   - askreddit (1% across all rules)
   - android, twoxchromosomes (1-2%)
   - leagueoflegends (0%)

## Files Generated
- `expansion_summary.csv` - Full results table
- `expansion_samples/` - Sample files (14 files)
- `expansion_results/` - Analysis results (14 files)
