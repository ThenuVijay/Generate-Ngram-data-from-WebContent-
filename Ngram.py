import urllib.request
import read as re

file = urllib.request.urlopen('https://ta.wikipedia.org/wiki/%E0%AE%A4%E0%AE%A9%E0%AE%BF%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%9F%E0%AF%8D%E0%AE%9F_%E0%AE%B5%E0%AE%BE%E0%AE%B4%E0%AF%8D%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AF%88')
file1 = file.read()
file.close()

text=re.fileread(file1)


re.Findgrams1(text,1)
re.Findgrams1(text,2)
