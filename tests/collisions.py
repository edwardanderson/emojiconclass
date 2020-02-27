'''
Check which Emojiconclass expressions collide
'''

import csv


seen = {}

with open('../content/catalogue.csv', 'r', encoding='utf-8') as inf:
    rows = csv.reader(inf)
    for uri, emojis, label in rows:
        # Ignore uncatalogued entries
        if not emojis:
            continue

        if emojis not in seen:
            seen[emojis] = (uri, label)
        else:
            collision = seen[emojis]
            b_uri, b_label = collision
            print(f'{emojis}\t{uri}\t{label}\n\t{b_uri}\t{b_label}\n')
