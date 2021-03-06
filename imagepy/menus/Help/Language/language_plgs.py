from sciapp import Source
from imagepy.core.engine import Free

class Language(Free):
	def __init__(self, key):
		self.title = key
		asyn = False

	#process
	def run(self, para = None):
		Manager.set(self.title)
		self.app.reload_plugins()

	def __call__(self):
		return self

plgs = [Language(i) for i in list(Source.manager('language').names())]
plgs.insert(0, Language('English'))
plgs.append('-')


class NewLanguage(Free):
	title = 'New Language'
	para = {'name':'your language'}
	view = [(str, 'name', 'name', '')]

	def run(self, para = None):
		LanguageManager.newdic(para['name'])
		LanguageManager.write()

class UpdateDictionary(Free):
	title = 'Update Dictionary'

	def run(self, para = None):
		LanguageManager.add()
		LanguageManager.write()

class CleanDictionary(Free):
	title = 'Clean Dictionary'

	def run(self, para = None):
		LanguageManager.rm()
		LanguageManager.write()

plgs.extend([NewLanguage, UpdateDictionary, CleanDictionary])

if __name__ == '__main__':
	print(list(ColorManager.luts.keys()))
    