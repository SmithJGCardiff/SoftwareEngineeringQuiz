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
			categories.append(newCat)
			db['cats'] = categories

	def getList():
		fname = 'categorydb'
		if os.path.isfile(fname):
			with shelve.open(fname,'r') as db:
				return db['cats']
		else:
			return ['Error FNF']

	def deleteCategory(catDel):
		with shelve.open('categorydb','w') as db:
			categories = db['cats']
			categories.remove(catDel)
			db['cats'] = categories

		with shelve.open('questiondb',writeback =True) as db:
			for questionID in db.keys():
				if catDel in db[questionID].category:

					tStr = db[questionID].category
					print(tStr)
					tStr = tStr.replace((catDel+" "),"")
					print('inCategoryafterReplaceis' + tStr)
					db[questionID].category = tStr

