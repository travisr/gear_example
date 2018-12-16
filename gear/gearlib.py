import json, os, sys

class Gear:
	def __init__(self):
		# Read config.json to get inputs and config options
		try:
			self.config_file = 'config.json'
			self.data = json.loads(open(self.config_file).read())
		except:
			print('ERROR: can\'t open file: ' + self.config_file)
			sys.stdout.flush()
			exit(1)

	def log(self, str):
		print(str)
		sys.stdout.flush()

	def __log_tree_dir(self, path):
		with os.scandir(path) as it:
			for entry in it:
				self.log(path + '/' + entry.name)
				if entry.is_dir():
					self.__log_tree_dir(path + '/' + entry.name)

	def log_tree(self, path):
		self.log('\nDirectory ' + path + ' contains:')
		self.__log_tree_dir(path)

	def log_cwd(self):
		self.log('\nCurrent working directory:')
		self.log(os.getcwd())

	def log_env(self):
		self.log('\nEnvironment variables:')
		for param in os.environ.keys():
			self.log(param + '=' + os.environ[param])		

	def log_data(self):
		self.log('\ngear.data (./config.json):')
		self.log(json.dumps(self.data, separators=(', ', ': '), sort_keys=True, indent=4))

	def log_all(self):
		self.log_env()
		self.log_cwd()
		self.log_tree('.')		
		self.log_data()

	def log_output(self):
		self.log_tree('./output')		

	def result_file(self, path):
		self.log('moving ' + path + ' to gear output')
		# move the file here

	def result_metadata(self, idobj, dictobj):
		self.log(json.dumps(idobj, separators=(', ', ': '), sort_keys=True, indent=4))
		self.log(json.dumps(dictobj, separators=(', ', ': '), sort_keys=True, indent=4))
		# write the metadata fie here