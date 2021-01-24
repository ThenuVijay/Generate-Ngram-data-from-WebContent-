import urllib.request
import read as re

file = urllib.request.urlopen('https://en.wikipedia.org/wiki/Life')
file1 = file.read()
file.close()

text=re.fileread(file1)


print(re.Findgrams(text,2)) 
print(re.Findgrams(text,3))



