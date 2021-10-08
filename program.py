# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:03:32 2021

@author: 4PF41LA_RS6
"""

import os
import copy

mylist = os.listdir("tweets_or")

sorted(mylist)

list_splitted = []

for d in mylist:
    list_splitted.append(d.split("t"))
    
tweets = []

for l in list_splitted:
    tweets.append([int(l[0]), int(l[1].split("_")[1].split("s")[0])])