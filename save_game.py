import shelve 


class Save(object):
	"""docstring for Save"""
	def __init__(self, name_save):
		super(Save, self).__init__()
		self.name_save = name_save

	def save(self, key, arg):
		with shelve.open(self.name_save) as states:
			states[key] = arg

	def load(self, key):
		with shelve.open(self.name_save) as states:
			return states[key]
		