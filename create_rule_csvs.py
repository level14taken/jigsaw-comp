import pandas as pd

rules_data = [
    {
        'rule_name': 'financial_advice',
        'subreddit_list': ['SUBREDDIT1', 'SUBREDDIT2'],
        'rule': 'no financial advice: we do not permit comments that make personal recommendations for investments, taxes, or careers.',
        'positive_example_1': 'Take a portion of that 20k and hire a CFP to plan your financial future. Easily the most bang for your buck.',
        'positive_example_2': 'The best way to use \'debt\' to make more money is to use short sales on securities. This is very risky, takes extensive research, and can lead to almost infinite losses – but if you\'re right you will make a lot of $$',
        'negative_example_1': 'Live on 10 an hour? I make 8.25 an hour, and live fine.',
        'negative_example_2': 'I didn\'t haggle with my latest job - they made an offer that was the top of my desired salary range plus had massively better benefits compared to my previous job. I likely could have gotten a few percent more out of them, but it might have soured my relationship with my boss. The offer they made was more than fair so I accepted it. It sounds like you\'re in the same position.'
    },
    {
        'rule_name': 'medical_advice',
        'subreddit_list': ['SUBREDDIT1', 'SUBREDDIT2'],
        'rule': 'no medical advice: do not offer or request specific medical advice, diagnoses, or treatment recommendations.',
        'positive_example_1': 'Overdosing is a really bad method. Use nitrogen or nembutal.',
        'positive_example_2': 'In my opinion, the drugs are not helping. I don\'t know your full story and am basing what I think off of what you\'ve told us, but I really think the depression medications are no good for your stability. You\'ve been subjected to some pretty terrible experiences and the meds are just numbing you to it all. Let alone every time you take those pills your reminded of these terrible things that happened that are making you take the pills.',
        'negative_example_1': 'Hey friend, feel free to PM me if you\'d like someone to talk to. I\'ll be around.',
        'negative_example_2': 'Thank you for your optimism! I felt super depressed today for no reason and came here to sulk. You made me feel a little better!'
    },
    {
        'rule_name': 'illegal_activity',
        'subreddit_list': ['SUBREDDIT1', 'SUBREDDIT2'],
        'rule': 'no promotion of illegal activity: do not encourage or promote illegal activities, such as drug-related activity, violence, exploitation, theft, or other criminal behavior.',
        'positive_example_1': 'Just rape her and hide her body, you work in a factory goddamnit',
        'positive_example_2': 'Why don\'t you blow your brains out with a shotgun, instead of giving me empty platitudes.',
        'negative_example_1': 'Sure there is, go to the gym, get some decent clothes, learn how to build up confidence, get a hobby or something interesting about yourself. Hell, it\'s fucking easy as shit to meet women these days with apps like Tinder. You\'re the same as HAES people saying it can\'t be done because you just can\'t be bothered to make the effort. It\'s your choice if you want to wallow in your own self pity or make something of yourself.',
        'negative_example_2': 'I think you should seek therapy. Everyone keeps telling you that you\'re not boring (you got picked because of your skills on the bass ffs) and that you\'re not unattractive, but you can\'t seem to believe it.'
    },
    {
        'rule_name': 'spoilers',
        'subreddit_list': ['SUBREDDIT1', 'SUBREDDIT2'],
        'rule': 'no spoilers: do not reveal important details that would limit people\'s ability to enjoy a show or movie.',
        'positive_example_1': 'Catelyn Stark brought back to life by Beric Dondarrion, who died in the process. She was found in the river by Nymeria (Arya\'s wolf, who Arya warged into at the time), then found by the BwB. She leads a far more ruthless BwB, and they begin intercepting Freys and killing them. They killed the Frey third in line of succession (just a child), another Frey in the epilogue of ASoS, the current Frey heir, etc. the guy with the yellow cloak that was killed by the Hound in the TV series is still a loyal member of the BwB and he is her right hand man. They catch Brienne and Pod and almost hang them (it\'s a cliffhanger at the end of AFFC), then send Brienne on a mission to capture Jaime to answer for his crimes against the Starks and Tullys.',
        'positive_example_2': 'Bastard Bowl in the North featuring the Vale. Tyrells vs Jesus Freaks in King\'s Landing. Dothraki+Unsullied vs Slaver\'s Bay, except Tyrion tried to be diplomatic with them. Tower of Joy and apparently more about the White Walkers as well. Arya becomes one of the faceless men.',
        'negative_example_1': 'Man the Hype is getting the better of me...',
        'negative_example_2': 'Get hype.'
    },
    {
        'rule_name': 'advertising',
        'subreddit_list': ['SUBREDDIT1', 'SUBREDDIT2'],
        'rule': 'No Advertising: Spam, referral links, unsolicited advertising, and promotional content are not allowed.',
        'positive_example_1': 'she will come your home open her legs with  and  you http://sh.ors.it/PALI2',
        'positive_example_2': 'code free tyrande --->>> [Imgur](http://i.imgur.com/KlvssCl.png)\n\nfor you and your friend 2 codes for 4 dollars https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UN4E27AG7BWKS\n\n2$... buy one directly from here: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=VP3S5HQRE7T7E',
        'negative_example_1': 'Banks don\'t want you to know this! Click here to know more!',
        'negative_example_2': 'SD Stream [ ENG Link 1] (http://www.sportsstreams247.com/astra-giurgiu-vs-fc-austria-wien/)'
    },
    {
        'rule_name': 'legal_advice',
        'subreddit_list': ['SUBREDDIT1', 'SUBREDDIT2'],
        'rule': 'No legal advice: Do not offer or request legal advice.',
        'positive_example_1': 'Lol. Try appealing the ban and say you won\'t do it again.',
        'positive_example_2': 'Maybe true, but that\'s very short-sighted. The lawsuits are already in the hundreds though on this. He\'s going to be getting sued six ways to sunset for his entire term. The Constitution offers very broad protection and it extends very far. Trump has no concept of what is involved.\n\nHe needs a judge that is a flexible Constitutionalist, not a literal one, because he\'s definitely going to bending the Constitution around in the next 4 years. He\'s already started.',
        'negative_example_1': 'I live in the US it\'s it possible to get in trouble for watching illegal streams?',
        'negative_example_2': 'Background checks are not always required. There are 33 states that allow people to buy from individuals without a check. \n\nThere is also no restrictions (that I know of) because of mental health. I could be wrong about that.'
    }
]

unlabelled = pd.read_csv('/home/manoj/my_projects/jigsaw/reddit-removal-log.csv')

for rule_data in rules_data:
    rule_name = rule_data['rule_name']
    subreddit_list = rule_data['subreddit_list']

    filtered_data = unlabelled[unlabelled['subreddit'].isin(subreddit_list)].copy()

    filtered_data['rule'] = rule_data['rule']
    filtered_data['positive_example_1'] = rule_data['positive_example_1']
    filtered_data['positive_example_2'] = rule_data['positive_example_2']
    filtered_data['negative_example_1'] = rule_data['negative_example_1']
    filtered_data['negative_example_2'] = rule_data['negative_example_2']
    filtered_data['rule_violation'] = ''

    if 'row_id' not in filtered_data.columns:
        filtered_data.insert(0, 'row_id', range(len(filtered_data)))

    columns_order = ['row_id', 'body', 'rule', 'subreddit', 'positive_example_1', 'positive_example_2', 'negative_example_1', 'negative_example_2', 'rule_violation']
    final_df = filtered_data[columns_order]

    csv_filename = f'/home/manoj/my_projects/jigsaw/rule_{rule_name}.csv'
    final_df.to_csv(csv_filename, index=False)
    print(f'Created: {csv_filename} with {len(final_df)} rows')
    print(f'  Subreddit placeholder: {subreddit_list}')

print('\n' + '='*80)
print('All 6 rule CSVs created successfully!')
print('='*80)
print('\nTo use: Edit the subreddit_list for each rule in the script, then run it.')
print('\nRules created:')
print('1. rule_financial_advice.csv')
print('2. rule_medical_advice.csv')
print('3. rule_illegal_activity.csv')
print('4. rule_spoilers.csv')
print('5. rule_advertising.csv')
print('6. rule_legal_advice.csv')
