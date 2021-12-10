# -*- coding: utf-8 -*-
# Advent Calendar of Code day 3

def to_int(lst):
    return int(''.join(map(str, lst)), 2)

lines = []
with open('03.txt') as file:
    lines = [list(map(int, i.strip())) for i in file.readlines()]

gamma = [int(sum(x) >= len(lines) / 2) for x in zip(*lines)]
epsilon = [1-i for i in gamma]

gamma_int = to_int(gamma)
epsilon_int = to_int(epsilon)

print(gamma_int * epsilon_int)

oxygen = lines.copy()
for i in range(len(oxygen[0])):
    oxy_gamma = [int(sum(x) >= len(oxygen) / 2) for x in zip(*oxygen)]
    oxygen = [x for x in oxygen if x[i] == oxy_gamma[i]]
    if len(oxygen) == 1:
        break
    
co2 = lines.copy()
for i in range(len(co2[0])):
    co2_gamma = [int(sum(x) > len(co2) / 2) for x in zip(*co2)]
    co2 = [x for x in co2 if x[i] != co2_gamma[i]]
    if len(co2) == 1:
        break

oxy_int = to_int(oxy_gamma)
co2_int = to_int(co2_gamma)

print(oxy_int * co2_int)