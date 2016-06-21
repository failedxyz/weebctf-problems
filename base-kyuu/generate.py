# -*- coding: cp932 -*-
import math,sys
from PIL import Image

flag = 'weeb{s4NsHa1n_hyP3!!}'

#B
#nozomi: 90
#eli: 88
#hanayo: 82
#kotori: 80
#honoka: 78
#maki: 78
#umi: 76
#rin: 75
#nico: 74 (71)

l = ['nico','rin','umi','maki','honoka','kotori','hanayo','eli','nozomi']
x = int(flag.encode('hex'),16)

res = []
hist = [0]*9

for i in range(int(math.log(x,9)),-1,-1):
    res.append(l[int(x/9**i)])
    hist[int(x/9**i)]+=1
    x%=9**i

imgs = map(Image.open, ['img/%s.jpg'%i for i in res])
w, h = zip(*(i.size for i in imgs))
new = Image.new('RGB', (sum(w), max(h)))

offset = 0
for i in imgs:
  new.paste(i,(offset,0))
  offset += i.size[0]

#maxsize = (8192,200)
#new.thumbnail(maxsize, Image.ANTIALIAS)
new.save("img/μ's.jpg")
