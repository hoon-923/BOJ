# -*- coding: utf-8 -*-
"""[2884번] 알람 시계.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Mpe8iQafslvebBn-NdDg4RRPWOcyn4U
"""

H, M = map(int,input().split())

if M < 45 and H != 0: print(H-1,M+15)
elif M < 45 and H == 0: print(H+23,M+15)
else: print(H,M-45)