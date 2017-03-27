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
		with shelve.open('categorydb','c') as db:
			if 'cats' not in db:
				db['cats'] = []
			categories = db['cats']
			return categories

	def deleteCategory(catDel):
		with shelve.open('categorydb','w') as db:
			categories = db['cats']
			categories.remove(catDel)
			db['cats'] = categories

		with shelve.open('questiondb','w',writeback =True) as db:
			for questionID in db.keys():
				if catDel in db[questionID].category:

					tStr = db[questionID].category
					print(tStr)
					tStr = tStr.replace((catDel+" "),"")
					print('inCategoryafterReplaceis' + tStr)
					db[questionID].category = tStr

	def questionCount(catCount):
		count = 0
		with shelve.open('questiondb','r') as db:
			for questionID in db.keys():
				if catCount in db[questionID].category:
					count+=1
					
		return count