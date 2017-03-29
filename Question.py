import shelve
class Question:
	def __init__(self, questionID="", category="", topics="",
		entQuestion="", entAnswer="",
		entA1="" , entA2="", entA3="",imageExt=""):
		self.questionID = questionID
		self.category = category
		self.topics = topics
		self.entQuestion = entQuestion
		self.entAnswer = entAnswer
		self.entA1 = entA1
		self.entA2 = entA2
		self.entA3 = entA3
		self.imageExt = imageExt

	def getQuestionText(qID):
		with shelve.open('questiondb','r') as db:
			qText = db[qID].entQuestion
		return qText
	def getQuestsfromCat(category):
		qs = []
		with shelve.open('questiondb','r') as db:
			for key in db.keys():
				if category in db[key].category:
					q = db[key]
					qs.append(q)
		return qs