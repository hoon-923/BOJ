# -*- coding: utf-8 -*-
"""[10430번] 나머지.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eevX7Vuq3JIKJK5HLkIm47QRX60cjo6t
"""

A, B, C = map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)