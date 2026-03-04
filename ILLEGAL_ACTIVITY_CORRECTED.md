# Illegal Activity Rule - Corrected Analysis

## The Problem
The initial wise file incorrectly targeted **piracy/copyright infringement** subreddits (soccerstreams, jailbreak) for the illegal_activity rule, when the rule actually targets:
- **Drug-related activity**
- **Violence**
- **Exploitation**
- **Theft**
- **Criminal behavior**

## New Analysis Results

### Overall Statistics
- **Total subreddits tested**: 7
- **Total comments analyzed**: 700
- **Total violations found**: 24
- **Overall violation rate**: 3.43%

### Results by Subreddit (Ranked)

| Rank | Subreddit | Violations | Rate | Assessment |
|------|-----------|------------|------|------------|
| 1 | **suicidewatch** | 10/100 | **10%** | ✅ BEST - Suicide method promotion, encouraging self-harm |
| 2 | **depression** | 4/100 | **4%** | ⚠️ MEDIUM - Some suicide encouragement, violence |
| 3 | **conspiracy** | 4/100 | **4%** | ⚠️ MEDIUM - Violence encouragement, suicide |
| 4 | syriancivilwar | 3/100 | 3% | ⚠️ LOW - Some violence promotion |
| 5 | shitredditsays | 2/100 | 2% | ❌ LOW - Minimal signal |
| 6 | socialism | 1/100 | 1% | ❌ VERY LOW - Almost no signal |
| 7 | latestagecapitalism | 0/100 | 0% | ❌ NO SIGNAL |

## Violation Types Found

### Suicidewatch (10 violations)
- Providing specific suicide methods (exit bag, nitrogen, Nembutal)
- Asking about suicide methods
- Directly telling people to kill themselves
- Encouraging suicide with specific advice
- Providing lethal drug dosage information

### Depression (4 violations)
- Encouraging suicide ("kill yourself")
- Promoting violence toward others
- Providing suicide method advice

### Conspiracy (4 violations)
- Encouraging suicide
- Promoting violence/murder
- Encouraging assault

### Syriancivilwar (3 violations)
- Promoting violence/deaths
- Celebrating killings
- Encouraging beheading

## Comparison with Previous Analysis

### ❌ INCORRECT (Piracy Focus):
- **soccerstreams**: 94% - Copyright infringement (illegal streaming)
- **jailbreak**: 15% - Software piracy, theft of apps/games

### ✅ CORRECT (Drugs/Violence/Exploitation):
- **suicidewatch**: 10% - Real criminal activity (assisted suicide, harm)
- **depression**: 4% - Violence, suicide encouragement
- **conspiracy**: 4% - Violence, suicide encouragement

## Recommendations

### For Production - Use These:
1. **suicidewatch** (10%) - Highest signal for illegal activity rule
2. **incels** (12% from previous analysis) - Also had violence/rape promotion

### Consider with Caution:
- depression (4%) - Some signal but lower
- conspiracy (4%) - Some signal but lower
- syriancivilwar (3%) - Borderline

### Do NOT Use:
- socialism, latestagecapitalism, shitredditsays - Too low signal
- soccerstreams, jailbreak - Wrong type of illegal activity (piracy)

## Key Takeaway

**The illegal_activity rule works best in subreddits with:**
- Mental health crisis discussions (suicide methods shared)
- Extremist communities (violence encouraged)
- Hate/toxic communities (harm promoted)

**Overall**: Real illegal activity (drugs/violence/exploitation) has **much lower rates** (3-10%) than piracy (94%), but is what the rule is actually targeting.

## Files Generated
- `illegal_activity_summary.csv` - Full results
- `illegal_samples/` - All sampled comments (7 files)
- `illegal_results/` - Individual analysis results (7 files)
