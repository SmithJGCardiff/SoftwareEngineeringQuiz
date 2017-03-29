import shelve
class Event:
	def __init__(self,eventName="",dateTime="",schools=[],category ="",questions={}):
		self.eventName =eventName
		self.dateTime = dateTime
		self.schools =schools
		self.questions =questions
		self.category =category


	def addQScores(qID,state,school):
		with shelve.open("eventslogdb",writeback = True) as db:
			questionScores = db["currentEvent"].questions
			if school in questionScores.keys():
				if qID in questionScores[school].keys():
					if state == "correct":
						questionScores[school][qID][0] += 1
					elif state == "incorrect":
						questionScores[school][qID][1] += 1
					elif state == "unanswered":
						questionScores[school][qID][2] += 1
				else:
					questionScores[school][qID] = [0,0,0]
					if state == "correct":
						questionScores[school][qID][0] += 1
					elif state == "incorrect":
						questionScores[school][qID][1] += 1
					elif state == "unanswered":
						questionScores[school][qID][2] += 1
			else:
				questionScores[school] = dict()
				questionScores[school][qID] = [0,0,0]

				if state == "correct":
					questionScores[school][qID][0] += 1
				elif state == "incorrect":
					questionScores[school][qID][1] += 1
				elif state == "unanswered":
					questionScores[school][qID][2] += 1
			db["currentEvent"].questions = questionScores

	def getCategory():
		try:
			with shelve.open("eventslogdb","r") as db:
				cat = db["currentEvent"].category
				if cat == "":
					return "No category selected"
				return cat
		except:
			return "No current event"


	def setCategory(selCat):
		with shelve.open("eventslogdb",writeback=True) as db:
			db["currentEvent"].category = selCat

	def getEventName():
		try:
			with shelve.open("eventslogdb","r") as db:
				name = db["currentEvent"].eventName
				return name
		except:
			return "No current event"


	def getSchools():
		with shelve.open("eventslogdb","r") as db:
			schools = db["currentEvent"].schools
			return schools