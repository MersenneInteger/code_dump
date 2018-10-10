#!/usr/bin/python

import json

with open('config.json') as fh:
    conf = json.load(fh)
print(conf)
displays = conf['Displays']
tps = conf['Touchpanels']
print(displays, tps)

with open('config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, seperators=(',',':'))
