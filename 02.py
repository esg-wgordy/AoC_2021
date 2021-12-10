# -*- coding: utf-8 -*-
# Advent Calendar of Code day 2

import pandas as pd

sub = pd.read_csv('02.txt', header=None, names=['dir', 'units'], sep=' ')
sub['horizontal'] = (sub['dir'] == 'forward') * sub['units']
sub['vertical'] = (sub['dir'] == 'up') * -sub['units'] + (sub['dir'] == 'down') * sub['units']

print(sum(sub['horizontal'])* sum(sub['vertical']))

aim = 0
depth = 0
for i, row in sub.iterrows():
    aim += + (row['dir'] == 'up') * -row['units'] + (row['dir'] == 'down') * row['units']
    depth += aim * (row['dir'] == 'forward') * row['units']
    
print(sum(sub['horizontal']) * depth)
