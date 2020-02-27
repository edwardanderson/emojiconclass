'''
Check which Emojiconclass expressions collide
'''

import csv


emojiconclasses = {}

with open('../content/catalogue.csv', 'r', encoding='utf-8') as inf:
    rows = csv.reader(inf)
    for r in rows:
        uri = r[0]
        emojis = r[1]
        label = r[2]
        if not emojis:
            continue

        if emojis not in emojiconclasses:
            emojiconclasses[emojis] = (uri, label)
        else:
            collision, collision_label = emojiconclasses[emojis]
            print(f'{emojis}\t{uri}\t{label}\n\t{collision}\t{collision_label}\n')
