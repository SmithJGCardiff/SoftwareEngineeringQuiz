import shelve
import os
class Category:
	def __init__(self,catName):
		name = catName

	def addCategory(newCat):
		with shelve.open('categorydb','c') as db:
			if 'cats' not in db:
				db['cats'] = []
			categories = db['cats']
			print(categories)
			print(newCat)
			categories.append(newCat)
			db['cats'] = categories

	def getList():
		fname = 'categorydb'
		if os.path.isfile(fname):
			with shelve.open(fname,'r') as db:
				return db['cats']
		else:
			return ['Error FNF']
