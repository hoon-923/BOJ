# -*- coding: utf-8 -*-
"""[14681번] 사분면 고르기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Mpe8iQafslvebBn-NdDg4RRPWOcyn4U
"""

x = int(input())
y = int(input())

if x>0 and y>0: print("1")
elif x<0 and y>0: print("2")
elif x<0 and y<0: print("3")
elif x>0 and y<0: print("4")