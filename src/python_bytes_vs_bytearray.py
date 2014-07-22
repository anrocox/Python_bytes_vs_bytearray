#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

What is the difference between bytes and bytearray object in Python?

¿Cual es la diferencia entre un objeto bytes y bytearray en Python?
'''

#bytearray objects are a mutable counterpart to bytes objects, support the
#mutable sequence operations in addition to the common of bytes objects.
ba = bytearray('bytearray is not mutable', 'utf8')
print(ba)

#can remove items from the bytes
del ba[13:17]
print(ba)

#can add items from the bytes
ba[9:9] = b' object'
print(ba)

#can use the methods of mutable type iterable objects as the lists
ba.append(33)
print(ba)
