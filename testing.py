

with open('IDList.txt','ab+') as f:
	fileStr = ''
	if f.tell() < 4:
		questionID = 1001 
	else:
		f.seek(-4,2)
		questionID = int(f.read()) + 1
		fileStr += '\n'
	f.write((str(questionID)).encode('utf-8'))



