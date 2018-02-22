

class Counter:
	def __init__(self):
		self._counter = 0
	
	def get_counter(self):
		return self._counter
	
	def add_one(self):
		self._counter += 1
	
	def take_one(self):
		self._counter -= 1

	def __str__(self):
		return "The counter is at: "+str(self._counter)
	

def create_counter():
	return Counter()

counters = list()

for counter in range(0, 20):
	counters.append(create_counter())
	counters[counter].add_one()
	

for con in counters:
	print(con)

