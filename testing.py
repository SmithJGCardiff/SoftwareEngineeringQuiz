import shelve
with shelve.open("eventslogdb") as db:
	for key in db.keys():
		print(key)
		if key != "currentEvent":
			print(db[key].questions)