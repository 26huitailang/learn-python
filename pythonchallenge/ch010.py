import re  
  
result='1'  
  
pattern=re.compile(r'((?P<w>\d)(?P=w)*)')  
  
for i in range(30):  
    a=map(lambda x:'%s%s'%(len(x[0]),x[1]),pattern.findall(result))  
    print pattern.findall(result),'\n'
    print a,'\n'
    result=''.join(a)  
    print result,'\n'
    
    
print len(result)  