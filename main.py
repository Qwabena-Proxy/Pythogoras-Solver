# importing math lib
from math import *

#Taking of input
print("X must be the input for the value you are finding for..")
print()
hypo = input("Hypotenuse : ")
adj = input("Adjacent : ")
opp = input("Opposite : ")

error_adj = 0
error_opp = 0
error_hyp = 0

if hypo.lower() == 'x':
    try:
        adj = int(adj)
    except ValueError as er_o:
        error_adj = 1
        print("Entry for Adjacent is not an interger")
    try:
        opp = int(opp)
    except ValueError as er_tt:
        error_opp = 1
        print("Entry for Opposite is not an interger")
    if error_adj == 0 and error_opp == 0:
        ans = sqrt((adj**2) + (opp ** 2))
        ans = str(ans).split(".")
        print(f'Hypotenuse : {ans[0]}')
    
elif adj.lower() == 'x':
    try:
        hypo = int(hypo)
    except ValueError as er_t:
        error_hyp = 1
        print("Entry for Hypotenuse is not an interger")
    try:
        opp = int(opp)
    except ValueError as er_tt:
        error_opp = 1
        print("Entry for Opposite is not an interger")
    if error_hyp == 0 and error_opp == 0:
        ans = sqrt((hypo**2) - (opp**2))
        ans = str(ans).split(".")
        print(f'Adjacent : {ans[0]}')
elif opp.lower() == 'x':
    try:
        hypo = int(hypo)
    except ValueError as er_t:
        error_hyp = 1
        print("Entry for Hypotenuse is not an interger")
    try:
        adj = int(adj)
    except ValueError as er_o:
        error_adj = 1
        print("Entry for Adjacent is not an interger")
    if error_adj == 0 and error_hyp == 0:
        ans = sqrt(-(adj**2) + (hypo**2))
        ans = str(ans).split(".")
        print(f'Opposite : {ans[0]}')
