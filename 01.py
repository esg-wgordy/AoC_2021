# -*- coding: utf-8 -*-
# Advent Calendar of Code day 1

import pandas as pd

depths = pd.read_csv('01.txt', header=None, names=['depth'])
depths['greater'] = depths['depth'] < depths['depth'].shift(-1)

print(sum(depths['greater']))

depths['rollingsum'] = depths['depth'].rolling(3).sum()
depths['rolling_greater'] = depths['rollingsum'] < depths['rollingsum'].shift(-1)

print(sum(depths['rolling_greater']))