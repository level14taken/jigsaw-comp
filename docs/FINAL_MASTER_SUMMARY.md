# MASTER SUMMARY - All 3 Rounds of Analysis

## Overall Statistics

### Round 1 (Initial Validation):
- Subreddit-rule combinations: 25
- Comments: 2,500
- Violations: 220 (8.8%)

### Round 2 (Expansion):
- Subreddit-rule combinations: 14
- Comments: 1,400
- Violations: 35 (2.5%)

### Round 3 (High-Potential):
- Subreddit-rule combinations: 15
- Comments: 1,500
- Violations: 45 (3.0%)

### **TOTAL ACROSS ALL ROUNDS**:
- **Subreddit-rule combinations: 54**
- **Comments analyzed: 5,400**
- **Violations found: 300**
- **Overall violation rate: 5.6%**

## 🏆 TOP 10 BEST SOURCES (All Time)

| Rank | Rule | Subreddit | Rate | Round |
|------|------|-----------|------|-------|
| 1 | spoilers | **anime** | **18%** | Round 1 |
| 2 | advertising | **videos** | **16%** | Round 3 🆕 |
| 3 | illegal_activity | **jailbreak** | **15%** | Round 1 (piracy*) |
| 4 | spoilers | **asoiaf** | **14%** | Round 1 |
| 5 | financial_advice | **personalfinance** | **13%** | Round 1 |
| 6 | illegal_activity | **incels** | **12%** | Round 1 |
| 7 | spoilers | **gameofthrones** | **11%** | Round 1 |
| 8 | illegal_activity | **suicidewatch** | **10%** | Illegal retest |
| 9 | medical_advice | **suicidewatch** | **7%** | Round 1 |
| 10 | advertising | **pcmasterrace** | **6%** | Round 2 |

*Note: jailbreak had 15% but was piracy, not drugs/violence

## 📊 FINAL PRODUCTION RECOMMENDATIONS

### Rule 1: Financial Advice
**Best source:**
- **personalfinance** (13%) ⭐ PRIMARY - ONLY strong source

**Honorable mentions:**
- lifeprotips (3%)
- relationships (2%)

**Verdict**: Limited sources. personalfinance is dominant.

---

### Rule 2: Medical Advice
**Best sources:**
- **suicidewatch** (7%) ⭐ PRIMARY
- **depression** (6%) ⭐ PRIMARY
- science (4%)
- relationships (4%)
- askscience (3%)

**Skip**: askreddit, askwomen, twoxchromosomes, lifeprotips, explainlikeimfive (<2%)

**Verdict**: Good variety of sources, especially mental health subreddits.

---

### Rule 3: Illegal Activity (drugs/violence/exploitation)
**Best sources:**
- **incels** (12%) ⭐ PRIMARY
- **suicidewatch** (10%) ⭐ PRIMARY
- worldnews (5%)

**Skip**: conspiracy, depression, political subs, latestagecapitalism (<5%)

**Verdict**: incels and suicidewatch are clearly the best. worldnews is decent backup.

---

### Rule 4: Spoilers
**Best sources:**
- **anime** (18%) ⭐⭐⭐ TOP SOURCE
- **asoiaf** (14%) ⭐ PRIMARY
- **gameofthrones** (11%) ⭐ PRIMARY
- television (4%)
- movies (3%)

**Skip**: books, nosleep, leagueoflegends, games (≤3%)

**Verdict**: Excellent sources. Anime is outstanding.

---

### Rule 5: Advertising 🆕
**Best sources:**
- **videos** (16%) ⭐⭐⭐ NEW TOP SOURCE!
- **pcmasterrace** (6%) ⭐ PRIMARY
- **pokemongo** (5%) ⭐ PRIMARY
- **gonewild** (5%) ⭐ PRIMARY (NSFW)

**Honorable mentions:**
- futurology, games, politics (3%)
- android (2%)

**Skip**: churning (0%)

**Verdict**: Excellent discovery! videos is a goldmine. Multiple good sources.

---

### Rule 6: Legal Advice 🆕
**Best source:**
- **relationships** (3%) - ONLY source found

**Skip**: askreddit, explainlikeimfive (≤1%)

**Verdict**: Limited signal. relationships is only viable source.

## 🎯 Production-Ready Sources (≥3% violation rate)

### Tier 1: Outstanding (≥10%)
1. anime @ spoilers (18%)
2. videos @ advertising (16%)
3. jailbreak @ illegal_activity (15% - but piracy)
4. asoiaf @ spoilers (14%)
5. personalfinance @ financial_advice (13%)
6. incels @ illegal_activity (12%)
7. gameofthrones @ spoilers (11%)
8. suicidewatch @ illegal_activity (10%)

### Tier 2: Excellent (5-9%)
9. suicidewatch @ medical_advice (7%)
10. depression @ medical_advice (6%)
11. pcmasterrace @ advertising (6%)
12. pokemongo @ advertising (5%)
13. gonewild @ advertising (5%)
14. worldnews @ illegal_activity (5%)

### Tier 3: Good (3-4%)
15. science @ medical_advice (4%)
16. relationships @ medical_advice (4%)
17. television @ spoilers (4%)
18. conspiracy @ illegal_activity (4%)
19. depression @ illegal_activity (4%)
20. askscience @ medical_advice (3%)
21. relationships @ legal_advice (3%)
22. movies @ spoilers (3%)
23. lifeprotips @ financial_advice (3%)
24. syriancivilwar @ illegal_activity (3%)
25. futurology @ advertising (3%)
26. games @ advertising (3%)
27. politics @ advertising (3%)
28. books @ spoilers (3%)

## 💡 Key Learnings

### What Worked Best:
1. **Mental health subreddits** - High signal for both medical advice and illegal activity
2. **Entertainment subreddits** - Excellent for spoilers (anime, GoT, asoiaf)
3. **Tech/gaming subreddits** - Good for advertising
4. **NSFW subreddits** - Good for advertising (gonewild)
5. **Videos subreddit** - HUGE win for advertising (16%)

### What Didn't Work:
1. **General Q&A subreddits** - askreddit, explainlikeimfive too generic (0-1%)
2. **Financial advice** - Very limited sources beyond personalfinance
3. **Legal advice** - Very low signal overall
4. **Piracy vs Real Crime** - Had to distinguish (jailbreak, soccerstreams were piracy, not drugs/violence)
5. **Gaming for spoilers** - Wrong type of content (industry talk, not story spoilers)

### Surprises:
1. **videos** - 16% advertising! Huge unexpected win
2. **explainlikeimfive** - Complete failure (0% across all rules)
3. **hillaryclinton** - 0% illegal activity (surprisingly civil)
4. **relationships** - Versatile source across multiple rules
5. **suicidewatch** - High signal for BOTH medical advice AND illegal activity

## 📁 All Files Generated

### Round 1:
- wise_validation_summary.csv
- VALIDATION_SUMMARY.md
- illegal_activity_summary.csv
- ILLEGAL_ACTIVITY_CORRECTED.md
- rule_violation_examples.txt

### Round 2:
- expansion_summary.csv
- EXPANSION_SUMMARY.md

### Round 3:
- round3_summary.csv
- ROUND3_SUMMARY.md

### Master:
- **FINAL_MASTER_SUMMARY.md** (this file)

## 🎬 Recommended Final Dataset

Based on all analysis, here are the subreddits to use in production:

### Tier 1 - Must Include (≥10%):
- anime (spoilers)
- videos (advertising)
- personalfinance (financial_advice)
- incels (illegal_activity)
- gameofthrones (spoilers)
- asoiaf (spoilers)
- suicidewatch (illegal_activity + medical_advice)

### Tier 2 - Strongly Recommended (5-9%):
- depression (medical_advice)
- pcmasterrace (advertising)
- pokemongo (advertising)
- gonewild (advertising)
- worldnews (illegal_activity)

### Tier 3 - Include if Need More Data (3-4%):
- science, relationships, television, askscience (various rules)

**Total estimated violations from top sources**: ~800-1000 violations from 2M comment dataset

## Next Steps

1. ✅ Extract full datasets from Tier 1 & 2 sources
2. ✅ Create training/validation split
3. ✅ Build classifier models
4. ⚠️ Consider: Do we want piracy violations? (jailbreak 15%, soccerstreams 94%)
5. ⚠️ Consider: NSFW content acceptable? (gonewild 5%)
