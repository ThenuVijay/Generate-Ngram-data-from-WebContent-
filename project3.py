import urllib.request
from read import *

file = urllib.request.urlopen('https://en.wikipedia.org/wiki/Life')
file1 = file.read()
file.close()

text=fileread(file1)


print(Findgrams(text,2)) 
print(Findgrams(text,3))



