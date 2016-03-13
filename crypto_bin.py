class BinaryCrypto:
	""" uses the famous openSSL to decrypt
	ADVANTAGES:
		- damn fast
	DISADVANTAGES:
		- how to supply bin variable to it? subprocess.Popen?
		otherwise it will have to open the file everytime
	"""
	
	binPath = "openssl"	# static var

	def __init__(self):
		with open("enc_params.config", mode="rt") as temp:
			x = temp.readlines()
		self.kbpdAlgo = 
		self.paddingAlgo = 
		return

	@classmethod
	def setBinPath(self):
		x = input("Enter path to openSSL binary")
		y = os.path.join(x, self.binPath)
		try:
			if subprocess.run(y + "version", stdout=subprocess.DEVNULL, \
			stderr=subprocess.DEVNULL).returncode == 0:
				self.binPath = y
				return True
		except FileNotFoundError:
			if input("Incorrect . . . Try again (Y/N)? ")[0] in "yY":
				self.setBinPath()
		return False

	@classmethod
	def decrypt(self, filePath, fileBinary, key):
		""" filePath is ignored if fileBinary is available (?and usable)
		"""

		return decryptedBinary

	@classmethod
	def encrypt(self, filePath):
		""" function defined only for testing purposes i.e.
		can breaker decrypt a file it as encrypt using the same(or another)
		util.
		"""
		key = "0123"
		root, ext = os.path.splitext(filePath)
		outFile = root + ".enc" + ext
		return outFile




