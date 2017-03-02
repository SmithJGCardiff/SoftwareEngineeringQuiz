import shelve
with shelve.open('questiondb') as db:
	print('number of questions: '+str(len(db)))
	for x in range(len(db)):
		print('question no: '+str(x))
		entry1 = db[str(x+1)]
		print(entry1.entQuestion)