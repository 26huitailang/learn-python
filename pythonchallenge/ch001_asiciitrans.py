'''
K-M
O-Q
E-G
every letter's asicii code +2
'''

hints = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

#print hints

def ltrans(l):
    if ord(l) in range(97,123):
        if ord(l)+2 < 123:
            l = chr(ord(l) +2)
        else:
            l = chr(ord(l) -24)
    return l

hints_trans = map(ltrans, hints)

print map(ltrans, 'map')
#print ''.join(hints_trans)
        
#write the translation in a txt file
fp = open(r'D:\github\learn-python\pythonchallenge\ch002.txt','w')
fp.write('The translation here: \n')
fp.write(''.join(hints_trans).capitalize())
fp.close()


