import shelve
with shelve.open('questiondb') as db:
	print(len(db))
	entry1 = db[str(1)]
	print(entry1.entQuestion)