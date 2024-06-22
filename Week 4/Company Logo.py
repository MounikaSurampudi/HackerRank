import math
import os
import random
import re
import sys



if __name__ == "__main__": 
    s = list(input())
    d = {el: s.count(el) for el in s}
    [print(occ, chars) 
         for occ, chars in sorted(d.items(), key= lambda x : (-x[1], x[0]))[:3]]
