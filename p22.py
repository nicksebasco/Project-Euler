"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
import re
from string import ascii_uppercase as abc

# lexographically score names \, max value set at 15 because max name length is 13
# adell, adella
def lex(word):
    score,i = [],0
    while i <= 15:
        if i < len(word):
            value = abc.index(word[i])
            value = str(value) if value > 9 else "0"+str(value)
            score.append(value)
        else:
            score.append("00")
        i = i + 1
    return int(reduce(lambda a,b: a+b,score))

# basic merge sort function
def mergex(arr,dic):
    if len(arr) > 1:
        m = len(arr)//2
        l,r = arr[0:m],arr[m:]
        mergex(l,dic)
        mergex(r,dic)
        i,j,k = 0,0,0
        while i < len(l) and j < len(r):
            if l[i] in r[j][0:len(l[i])]:
                arr[k] = l[i]
                i = i + 1
            elif r[j] in l[i][0:len(r[j])]:
                arr[k] = r[j]
                j = j + 1
            elif dic[l[i]] < dic[r[j]]:
                arr[k] = l[i]
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
            k = k + 1
        while i < len(l):
            arr[k] = l[i]
            i = i + 1
            k = k + 1
        while j < len(r):
            arr[k] = r[j]
            j = j + 1
            k = k + 1

def get_score(arr):
    total = 0
    for i in range(len(arr)):
        total = total + (i+1) * sum([abc.index(w)+1 for w in arr[i]])
    return total

def main():
    text_file = open('names.txt', 'r')
    text = text_file.read()
    text = re.sub('["\n]','', text)
    dic = {word:lex(word) for word in text.split(",")}
    keys = dic.keys()

    mergex(keys,dic)
    print "keys: ",keys, len(keys)
    print "score: ",get_score(keys)

main()

"""
# alternatively
from string import ascii_uppercase
from re import sub
score = lambda word: sum(ascii_uppercase.index(c) + 1 for c in word)
with open('names.txt') as f:
  names = sorted([sub('["\n]','', name) for name in f.read().split(',')])
  print sum(i*score(x) for i, x in enumerate(names, 1))
"""
