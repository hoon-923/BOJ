# -*- coding: utf-8 -*-
"""[2753번] 윤년.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Mpe8iQafslvebBn-NdDg4RRPWOcyn4U
"""

year = int(input())

if year%4 == 0 and year%100 != 0: print("1")
elif year%4 == 0 and year%400 == 0: print("1")
else: print("0")