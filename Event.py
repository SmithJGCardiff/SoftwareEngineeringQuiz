import shelve
class Event:
	def __init__(self,eventName="",dateTime="",schools=[],category ="",questions={}):
		self.eventName =eventName
		self.dateTime = dateTime
		self.schools =schools
		self.questions =questions
		self.category =category


	def addQScores(qID,state):
		with shelve.open("eventslogdb",writeback = True) as db:
			questionScores = db["currentEvent"].questions
			if qID in questionScores.keys():
				if state == "correct":
					questionScores[qID][0] += 1
				elif state == "incorrect":
					questionScores[qID][1] += 1
				elif state == "unanswered":
					questionScores[qID][2] += 1
			else:
				questionScores[qID] = [0,0,0]
				if state == "correct":
					questionScores[qID][0] += 1
				elif state == "incorrect":
					questionScores[qID][1] += 1
				elif state == "unanswered":
					questionScores[qID][2] += 1
			db["currentEvent"].questions = questionScores

	def getCategory():
		try:
			with shelve.open("eventslogdb","r") as db:
				cat = db["currentEvent"].category
				return cat
		except KeyError:
			return "No current event"

	def setCategory(selCat):
		with shelve.open("eventslogdb",writeback=True) as db:
			db["currentEvent"].category = selCat

	def getEventName():
		try:
			with shelve.open("eventslogdb","r") as db:
				name = db["currentEvent"].eventName
				return name
		except KeyError:
			return "No current event"