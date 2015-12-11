'''
find rare characters in the mess below: ch003.txt
'''

##fp = open(r'D:\github\learn-python\pythonchallenge\ch003.txt','r')
##s = fp.read()
####for line in lines:
####    print line
##fp.close()
##
##characters = set(s)
##chList = [i for i in characters]
##
###chList is the list of elements in ch003.txt, now to count
##d=dict()
##for i in range(len(chList)):
##    num = 0
##    for j in range(len(s)):
##        if s[j] == chList[i]:
##            num+=1
##            j+=1
##        else:
##            j+=1
##    d[chList[i]]=num
##    i+=1
##
##print sorted(d.items(), key = lambda d:d[1])

#thats the simple one
s = ''.join([line.rstrip() for line in open('ch003.txt')])    # no '/n' here
OCCURRENCES = {}
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
avgOC = len(s) // len(OCCURRENCES)
print ''.join([c for c in s if OCCURRENCES[c] < avgOC])     # equality

###third edition
##data = ''.join([line.rstrip() for line in open('ocr.txt')])    
##OCCURRENCES = collections.OrderedDict()
##for c in data: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
##avgOC = len(data) // len(OCCURRENCES)
##print ''.join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC])

##from string import ascii_letters
##import re, urllib2, webbrowser as wb
##print 'start'
##wb.open('http://www.pythonchallenge.com/pc/def/%s.html' %
##        ''.join(chr for chr in
##        re.findall('a-zA-Z',
##        urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
##        .read(), re.S) if chr in ascii_letters))
##
