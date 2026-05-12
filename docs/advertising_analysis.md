# Advertising Rule - Subreddit Analysis & Hypothesis

## Rule Definition
**"no advertising: spam, referral links, unsolicited advertising, and promotional content are not allowed."**

This includes:
- Spam messages
- Referral links (affiliate links, promo codes)
- Unsolicited advertising (selling products/services)
- Promotional content (self-promotion, brand promotion)

## Analysis: Where Are Advertising Violations Most Likely?

### HIGH PRIORITY - Very Likely to Have Advertising Violations

**1. churning (8,044 comments)**
- **Why**: Subreddit about credit card rewards/churning
- **Expected violations**: Referral links for credit cards, affiliate links, promotional codes
- **Confidence**: VERY HIGH (90%+)
- **Rationale**: Entire community built around sharing credit card signup bonuses - referral links are endemic

**2. pokemontrades (14,144 comments)**
- **Why**: Trading subreddit where people exchange Pokemon
- **Expected violations**: Selling Pokemon, advertising trading services, external site links
- **Confidence**: HIGH (60-70%)
- **Rationale**: Trading communities attract sellers and scammers

**3. GlobalOffensiveTrade (12,751 comments)**
- **Why**: CS:GO skin trading subreddit
- **Expected violations**: Selling skins, advertising trading sites, referral links to gambling sites
- **Confidence**: VERY HIGH (80%+)
- **Rationale**: Real money trading attracts advertisers and scammers

**4. personalfinance (22,841 comments)**
- **Why**: Financial advice subreddit
- **Expected violations**: Advertising financial services, promoting investment platforms, MLM schemes
- **Confidence**: MEDIUM-HIGH (50-60%)
- **Rationale**: Attracts financial service providers, insurance salespeople, MLM recruiters

**5. legaladvice (13,813 comments)**
- **Why**: Legal advice subreddit
- **Expected violations**: Lawyers advertising services, promoting legal services
- **Confidence**: MEDIUM (40-50%)
- **Rationale**: Professional service providers may advertise

### MEDIUM PRIORITY - Moderately Likely

**6. DIY (11,187 comments)**
- **Why**: Home improvement/DIY projects
- **Expected violations**: Product links, tool recommendations with affiliate links, contractor advertising
- **Confidence**: MEDIUM (40-50%)

**7. Android (10,650 comments)**
- **Why**: Android phone/app discussion
- **Expected violations**: App promotion, accessory sales, affiliate links
- **Confidence**: MEDIUM (40-50%)

**8. technology (6,768 comments)**
- **Why**: Tech news and discussion
- **Expected violations**: Product promotion, startup advertising, affiliate links
- **Confidence**: MEDIUM (30-40%)

**9. food (9,960 comments)**
- **Why**: Food photos and recipes
- **Expected violations**: Restaurant promotion, food blog links, cookbook sales
- **Confidence**: MEDIUM (30-40%)

**10. pcmasterrace (16,986 comments)**
- **Why**: PC gaming/building community
- **Expected violations**: Selling PC parts, promoting builds, affiliate links
- **Confidence**: MEDIUM (40-50%)

### LOWER PRIORITY - Some Expected

**11. Futurology (16,213 comments)**
- **Why**: Future tech discussion
- **Expected violations**: Startup promotion, cryptocurrency schemes
- **Confidence**: LOW-MEDIUM (20-30%)

**12. GetMotivated (5,823 comments)**
- **Why**: Motivational content
- **Expected violations**: Self-help book promotion, coaching services, MLM schemes
- **Confidence**: MEDIUM (40-50%)

**13. IAmA (6,030 comments)**
- **Why**: Celebrity/professional AMAs
- **Expected violations**: Self-promotion during AMAs, product plugs
- **Confidence**: LOW-MEDIUM (20-30%)

**14. LifeProTips (6,827 comments)**
- **Why**: Life advice subreddit
- **Expected violations**: Product recommendations with affiliate links, service promotion
- **Confidence**: LOW-MEDIUM (20-30%)

## Recommended Testing Order

### Tier 1 - Test First (Highest Expected Rates)
1. **churning** - VERY HIGH confidence (referral links)
2. **GlobalOffensiveTrade** - VERY HIGH confidence (trading/selling)
3. **pokemontrades** - HIGH confidence (trading/selling)

### Tier 2 - Test Second
4. **personalfinance** - MEDIUM-HIGH confidence (financial services)
5. **pcmasterrace** - MEDIUM confidence (PC parts/affiliate links)
6. **GetMotivated** - MEDIUM confidence (self-help/MLM)

### Tier 3 - Test If Needed
7. **DIY** - MEDIUM confidence
8. **Android** - MEDIUM confidence
9. **legaladvice** - MEDIUM confidence

## Key Patterns to Look For

**Referral Links:**
- "Use my link for bonus points"
- Shortened URLs (bit.ly, etc.)
- Affiliate codes

**Direct Sales:**
- "PM me if interested"
- "Check out my [product/service]"
- Price listings

**Self-Promotion:**
- "I created this app/website..."
- Blog/YouTube channel links
- Social media promotion

**MLM/Scams:**
- "Work from home opportunity"
- "DM me for details"
- Cryptocurrency schemes

## Expected Overall Rate
Based on the nature of these subreddits, I expect:
- **churning**: 50-80% violation rate (referral culture)
- **GlobalOffensiveTrade**: 40-60% violation rate (trading culture)
- **pokemontrades**: 30-50% violation rate (trading culture)
- **personalfinance**: 10-30% violation rate (mixed content)
- **Others**: 5-20% violation rate

## Why These Subreddits?

The common thread is **economic incentive**:
1. **Trading communities** - People trying to sell/profit
2. **Financial communities** - Service providers advertising
3. **Tech/product communities** - Affiliate marketing
4. **Self-improvement communities** - MLM/coaching schemes

These are all places where people have financial reasons to spam/advertise.
