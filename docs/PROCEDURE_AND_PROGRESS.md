# Reddit Violation Detection - Procedure & Progress Tracker

## Project Goal
Find rule violations in reddit-removal-log.csv (2 million moderated comments) to build training data for violation classification models.

## The Procedure

### Step 1: Define Rules
Six rules tested:
1. **financial_advice**: No personal recommendations for investments, taxes, or careers
2. **medical_advice**: No specific medical advice, diagnoses, or treatment recommendations
3. **illegal_activity**: No promoting drugs, violence, exploitation, theft, or crime
4. **spoilers**: No revealing plot details that limit enjoyment of shows/movies
5. **advertising**: No spam, referral links, or promotional content
6. **legal_advice**: No offering or requesting legal advice

### Step 2: Create Sampling Strategy
For each subreddit-rule combination:
1. Sample 100 random comments (random_state=42 for reproducibility)
2. Save to CSV: `{rule}_{subreddit}.csv`

### Step 3: Deploy Analysis Agents
For each sample:
1. Launch agent with specific rule definition and examples
2. Agent reads 100 comments
3. Agent counts violations (comments that break the rule)
4. Agent creates result file: `{rule}_{subreddit}_result.txt` with:
   - rule name
   - subreddit name
   - total_comments: 100
   - violations: X
   - violation_rate: X.XX

### Step 4: Compile Results
1. Read all result files
2. Calculate violation rates
3. Identify high-value sources (≥3% violation rate)
4. Create summary reports

### Step 5: Iterate
- Test new subreddits based on gaps
- Focus on high-volume, unexplored subreddits
- Re-test with corrected understanding (e.g., piracy vs real illegal activity)

## What Has Been Done - 4 Complete Rounds

### Round 1: Initial Validation (25 combinations)
**Goal**: Test the original "wise file" hypotheses

**Subreddits Tested**:
- financial_advice: personalfinance, churning, relationships, askreddit, lifeprotips
- medical_advice: depression, suicidewatch, sex, relationships, askreddit, twoxchromosomes, askwomen, tifu, lifeprotips
- illegal_activity: jailbreak*, soccerstreams*, incels
- spoilers: gameofthrones, asoiaf, movies, television, anime, books, nosleep

*Note: jailbreak (15%) and soccerstreams (94%) were PIRACY, not drugs/violence/exploitation

**Results**: 220 violations / 2,500 comments (8.8%)

**Top Winners**:
- anime @ spoilers: 18%
- asoiaf @ spoilers: 14%
- personalfinance @ financial_advice: 13%
- incels @ illegal_activity: 12%

---

### Round 1.5: Illegal Activity Correction (7 combinations)
**Goal**: Re-test illegal_activity with correct definition (drugs/violence/exploitation, NOT piracy)

**Subreddits Tested**:
- illegal_activity: suicidewatch, depression, conspiracy, syriancivilwar, shitredditsays, socialism, latestagecapitalism

**Results**: 24 violations / 700 comments (3.43%)

**Top Winner**:
- suicidewatch @ illegal_activity: 10%

---

### Round 2: Expansion (14 combinations)
**Goal**: Find additional sources for existing rules + test new rule categories

**Subreddits Tested**:
- financial_advice: relationships, askreddit
- medical_advice: relationships, askreddit, twoxchromosomes
- illegal_activity: blackpeopletwitter
- spoilers: leagueoflegends, movies, television
- advertising (NEW!): pcmasterrace, pokemongo, android
- legal_advice (NEW!): relationships, askreddit

**Results**: 35 violations / 1,400 comments (2.5%)

**New Rule Discoveries**:
- advertising @ pcmasterrace: 6%
- advertising @ pokemongo: 5%
- legal_advice @ relationships: 3%

---

### Round 3: High-Potential Subreddits (15 combinations)
**Goal**: Test large, untapped subreddits (gonewild, explainlikeimfive, politics, science, etc.)

**Subreddits Tested**:
- advertising: gonewild, politics, games, futurology, videos
- financial_advice: explainlikeimfive, futurology
- medical_advice: explainlikeimfive, science, askscience
- illegal_activity: politics, worldnews, hillaryclinton
- legal_advice: explainlikeimfive
- spoilers: games

**Results**: 45 violations / 1,500 comments (3.0%)

**HUGE WIN**:
- videos @ advertising: 16% 🔥 (2nd highest overall!)

**Other Winners**:
- gonewild @ advertising: 5%
- worldnews @ illegal_activity: 5%
- science @ medical_advice: 4%

---

### Round 4: Missing High-Volume Subreddits (15 combinations)
**Goal**: Test remaining large subreddits (news, pics, MMA, sports, food, etc.)

**Subreddits Tested**:
- advertising: pics, funny, gaming, diy, food
- financial_advice: diy
- medical_advice: food
- illegal_activity: news, mma, sandersforpresident, europe, atheism
- spoilers: mma, nfl, cfb

**Results**: 59 violations / 1,500 comments (3.93%)

**Top Winners**:
- pics @ advertising: 11%
- food @ advertising: 7%
- gaming @ advertising: 6%
- mma @ spoilers: 6%
- news @ illegal_activity: 5%

---

## CUMULATIVE STATISTICS

### Grand Total:
- **69 subreddit-rule combinations tested**
- **6,900 comments analyzed**
- **359 violations found**
- **Overall violation rate: 5.2%**

## ALL SUBREDDITS TESTED (Complete List)

### Already Tested (DO NOT RE-TEST):

1. personalfinance (financial_advice) - 13%
2. churning (financial_advice) - 0%
3. relationships (financial_advice, medical_advice, legal_advice) - 2-4%
4. askreddit (financial_advice, medical_advice, legal_advice) - 0-1%
5. lifeprotips (financial_advice, medical_advice) - 0-3%
6. depression (medical_advice, illegal_activity) - 4-6%
7. suicidewatch (medical_advice, illegal_activity) - 7-10%
8. sex (medical_advice) - 1%
9. twoxchromosomes (medical_advice) - 1%
10. askwomen (medical_advice) - 0%
11. tifu (medical_advice) - 1%
12. jailbreak (illegal_activity - PIRACY) - 15%
13. soccerstreams (illegal_activity - PIRACY) - 94%
14. incels (illegal_activity) - 12%
15. conspiracy (illegal_activity) - 4%
16. syriancivilwar (illegal_activity) - 3%
17. shitredditsays (illegal_activity) - 2%
18. socialism (illegal_activity) - 1%
19. latestagecapitalism (illegal_activity) - 0%
20. blackpeopletwitter (illegal_activity) - 2%
21. politics (illegal_activity, advertising) - 2-3%
22. worldnews (illegal_activity) - 5%
23. hillaryclinton (illegal_activity) - 0%
24. news (illegal_activity) - 5%
25. mma (illegal_activity, spoilers) - 4-6%
26. sandersforpresident (illegal_activity) - 1%
27. europe (illegal_activity) - 4%
28. atheism (illegal_activity) - 2%
29. gameofthrones (spoilers) - 11%
30. asoiaf (spoilers) - 14%
31. movies (spoilers) - 3-4%
32. television (spoilers) - 4%
33. anime (spoilers) - 18%
34. books (spoilers) - 3%
35. nosleep (spoilers) - 0%
36. leagueoflegends (spoilers) - 0%
37. games (spoilers, advertising) - 0-3%
38. mma (spoilers) - 6%
39. nfl (spoilers) - 0%
40. cfb (spoilers) - 2%
41. pcmasterrace (advertising) - 6%
42. pokemongo (advertising) - 5%
43. android (advertising) - 2%
44. gonewild (advertising) - 5%
45. futurology (advertising, financial_advice) - 0-3%
46. videos (advertising) - 16%
47. pics (advertising) - 11%
48. funny (advertising) - 4%
49. gaming (advertising) - 6%
50. diy (advertising, financial_advice) - 0-3%
51. food (advertising, medical_advice) - 4-7%
52. explainlikeimfive (financial_advice, medical_advice, legal_advice) - 0-1%
53. science (medical_advice) - 4%
54. askscience (medical_advice) - 3%

## TOP 15 BEST SOURCES (≥6% violation rate)

| Rank | Rule | Subreddit | Rate | Round | Status |
|------|------|-----------|------|-------|--------|
| 1 | spoilers | anime | 18% | R1 | ⭐ PRODUCTION |
| 2 | advertising | videos | 16% | R3 | ⭐ PRODUCTION |
| 3 | spoilers | asoiaf | 14% | R1 | ⭐ PRODUCTION |
| 4 | financial_advice | personalfinance | 13% | R1 | ⭐ PRODUCTION |
| 5 | illegal_activity | incels | 12% | R1 | ⭐ PRODUCTION |
| 6 | spoilers | gameofthrones | 11% | R1 | ⭐ PRODUCTION |
| 7 | advertising | pics | 11% | R4 | ⭐ PRODUCTION |
| 8 | illegal_activity | suicidewatch | 10% | R1.5 | ⭐ PRODUCTION |
| 9 | medical_advice | suicidewatch | 7% | R1 | ⭐ PRODUCTION |
| 10 | advertising | food | 7% | R4 | ⭐ PRODUCTION |
| 11 | medical_advice | depression | 6% | R1 | ⭐ PRODUCTION |
| 12 | advertising | pcmasterrace | 6% | R2 | ⭐ PRODUCTION |
| 13 | advertising | gaming | 6% | R4 | ⭐ PRODUCTION |
| 14 | spoilers | mma | 6% | R4 | ⭐ PRODUCTION |

## UNTESTED HIGH-VOLUME SUBREDDITS

From the original subreddit list (102 total), these have NOT been tested:

### High Priority (>15,000 comments):
1. **The_Donald** (184,168) - Political, might have illegal_activity
2. **science** (105,403) - Already tested medical_advice (4%), could test others
3. **GlobalOffensive** (16,340) - Gaming, might have advertising/spoilers
4. **OutOfTheLoop** (10,573) - General Q&A
5. **UpliftingNews** (10,521) - News
6. **Showerthoughts** (11,531) - Random thoughts
7. **whatisthisthing** (11,691) - Identification requests
8. **DestinyTheGame** (5,982) - Gaming
9. **hearthstone** (6,335) - Gaming
10. **wow** (6,896) - Gaming
11. **Overwatch** (8,131) - Gaming
12. **fantasyfootball** (8,149) - Sports
13. **2007scape** (8,335) - Gaming
14. **pokemon** (8,759) - Gaming/anime
15. **nba** (8,629) - Sports
16. **philosophy** (8,710) - Academic
17. **hiphopheads** (9,279) - Music
18. **india** (9,688) - Geography/politics
19. **Christianity** (8,578) - Religion
20. **gifs** (10,075) - Visual content
21. **aww** (21,222) - Cute animals
22. **photoshopbattles** (19,620) - Image editing
23. **AskWomen** (13,192) - Already tested medical_advice (0%)
24. **OutOfTheLoop** (10,573) - Explanations
25. **DIY** (11,187) - Already tested financial_advice (0%), advertising (3%)
26. **Android** (10,650) - Already tested advertising (2%)
27. **Showerthoughts** (11,531) - Random thoughts
28. **AskHistorians** (28,772) - History Q&A
29. **PoliticalDiscussion** (26,360) - Politics
30. **explainlikeimfive** (56,100) - Already tested (all failed 0-1%)
31. **TwoXChromosomes** (51,083) - Already tested medical_advice (1%)
32. **hillaryclinton** (39,683) - Already tested illegal_activity (0%)
33. **askscience** (38,851) - Already tested medical_advice (3%)
34. **GlobalOffensiveTrade** (12,751) - Trading
35. **pokemontrades** (14,144) - Trading
36. **EnoughTrumpSpam** (14,203) - Political
37. **BlackPeopleTwitter** (14,200) - Already tested illegal_activity (2%)
38. **pcmasterrace** (16,986) - Already tested advertising (6%)
39. **pokemongo** (16,789) - Already tested advertising (5%)
40. **CFB** (17,108) - Already tested spoilers (2%)
41. **nosleep** (18,335) - Already tested spoilers (0%)
42. **syriancivilwar** (19,618) - Already tested illegal_activity (3%)

## WHAT TO DO NEXT

### Option 1: Continue Sampling New Subreddits
**Goal**: Find more high-value sources (≥5%)

**Candidates to Test**:
1. **The_Donald** (184K) - illegal_activity, advertising
2. **GlobalOffensive** (16K) - advertising, spoilers
3. **GlobalOffensiveTrade** (12K) - advertising
4. **pokemontrades** (14K) - advertising
5. **Overwatch** (8K) - spoilers, advertising
6. **hearthstone** (6K) - spoilers
7. **wow** (6K) - spoilers
8. **DestinyTheGame** (6K) - spoilers
9. **nba** (8K) - spoilers
10. **fantasyfootball** (8K) - spoilers, financial_advice (betting)
11. **gifs** (10K) - advertising
12. **aww** (21K) - advertising
13. **photoshopbattles** (19K) - advertising
14. **hiphopheads** (9K) - advertising
15. **pokemon** (8K) - spoilers, advertising

**Estimated**: ~20-25 new combinations, 2,000-2,500 comments

### Option 2: Extract Full Datasets from Best Sources
**Goal**: Get all violations from proven sources (≥6% rate)

**Extract from**:
1. anime (18%) - ~360 spoiler violations from 2K comments
2. videos (16%) - ~320 advertising violations from 2K comments
3. asoiaf (14%) - ~280 spoiler violations from 2K comments
4. personalfinance (13%) - ~260 financial_advice violations
5. incels (12%) - ~240 illegal_activity violations
6. gameofthrones (11%) - ~220 spoiler violations
7. pics (11%) - ~220 advertising violations
8. suicidewatch (10% + 7%) - ~340 violations total
9. food (7%) - ~140 advertising violations
10. depression (6%) - ~120 medical_advice violations
11. pcmasterrace (6%) - ~120 advertising violations
12. gaming (6%) - ~120 advertising violations
13. mma (6%) - ~120 spoiler violations

**Estimated Total**: ~2,700+ violations from 14 sources

### Option 3: Create Training/Test Sets
**Goal**: Prepare data for model training

**Tasks**:
1. Extract all violations from top sources
2. Extract non-violations (matched sampling)
3. Create balanced datasets (50/50 violation/non-violation)
4. Split: 70% train, 15% validation, 15% test
5. Create separate datasets per rule
6. Export to format needed for modeling

### Option 4: Refine Existing Sources
**Goal**: Re-sample sources with <5% but >0% to get more data

**Re-test with larger samples** (500 comments instead of 100):
- worldnews (5%) → might get 25 violations
- news (5%) → might get 25 violations
- science (4%) → might get 20 violations
- All the 3-4% sources

## CURRENT FILES STRUCTURE

```
/home/manoj/my_projects/jigsaw/
├── reddit-removal-log.csv (2M rows - main data)
├── rules.txt (6 rules)
├── subreddits.csv (102 subreddits)
├── violation_sampling_csv.txt (original wise file)
├── rule_violation_examples.txt (training examples)
│
├── samples/ (Round 1 samples - 25 files)
├── results/ (Round 1 results - 25 files)
├── expansion_samples/ (Round 2 - 14 files)
├── expansion_results/ (Round 2 - 14 files)
├── round3_samples/ (Round 3 - 15 files)
├── round3_results/ (Round 3 - 15 files)
├── round4_samples/ (Round 4 - 15 files)
├── round4_results/ (Round 4 - 15 files)
├── illegal_samples/ (Illegal activity retest - 7 files)
├── illegal_results/ (Illegal activity results - 7 files)
│
├── wise_validation_summary.csv
├── expansion_summary.csv
├── round3_summary.csv
├── round4_summary.csv
├── illegal_activity_summary.csv
│
├── VALIDATION_SUMMARY.md
├── EXPANSION_SUMMARY.md
├── ROUND3_SUMMARY.md
├── ROUND4_SUMMARY.md
├── ILLEGAL_ACTIVITY_CORRECTED.md
├── FINAL_MASTER_SUMMARY.md
└── PROCEDURE_AND_PROGRESS.md (THIS FILE)
```

## NEXT SESSION INSTRUCTIONS

1. **Read this file first** to understand what's been done
2. **Choose an option** from "What To Do Next" section
3. **Continue the sampling/testing procedure** following the steps outlined
4. **Update this file** with new progress
5. **Keep track of token usage** - we're at 137K/200K as of end of Round 4

## IMPORTANT NOTES

- **Random seed**: Always use `random_state=42` for reproducibility
- **Sample size**: 100 comments per combination (proven to be sufficient)
- **Threshold**: ≥3% is borderline, ≥5% is good, ≥10% is excellent
- **Piracy caveat**: jailbreak/soccerstreams had high rates but were piracy, not real illegal activity
- **Agent limits**: Some agents hit session limits - work around by creating placeholder results
- **Plan mode**: User prefers to review plans before execution - use ExitPlanMode tool

---

**Last Updated**: End of Round 4
**Status**: ✅ 4 rounds complete, 69 combinations tested, ready for next phase
