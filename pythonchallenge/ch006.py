import zipfile,re  
  
z=zipfile.ZipFile('channel.zip','r')  
  
value=90052  
  
findNothing = re.compile(r'(?<=Next nothing is )\d+').search  
  
comments=[]
# raw_input()
while True:  
	content=z.read('%s.txt'%value)  
	comments.append(z.getinfo('%s.txt'%value).comment) 
	# print z.getinfo('%s.txt'%value).comment
	# raw_input()
	match=findNothing(content)  
	# match=apply(findNothing,(content,))  
	if match:  
		value=match.group(0)  
	else:  
		break  
	print content 
  
print z.read('%s.txt'%value)  
  
print ''.join(comments)