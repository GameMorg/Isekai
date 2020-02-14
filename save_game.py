import shelve 


class Save(object):
	"""
	сохранение данных
	"""
	def __init__(self, name_save):
		"""
		создает файл сохранения, с заданным названием
		:param name_save:
		"""
		super(Save, self).__init__()
		self.name_save = name_save

	def save(self, key, arg):
		"""
		сохраняет заданную информацию по заданному ключу,
		:param key:
		:param arg:
		:return:
		"""
		with shelve.open(self.name_save) as states:
			states[key] = arg

	def load(self, key):
		"""
		функция возвращает данные по заданному ключу
		:param key:
		:return:
		"""
		with shelve.open(self.name_save) as states:
			return states[key]
		