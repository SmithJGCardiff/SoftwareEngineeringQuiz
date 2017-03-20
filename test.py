import shelve
with shelve.open('questiondb',writeback = True) as db:
	for key in db.keys():
		print(db[key].entQuestion)
		db[key].category = ""