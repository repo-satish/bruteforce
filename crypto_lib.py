class LibraryCrypto:
	""" decrypt using wbond's oscrypto library
	ADVANTAGES:
		- faster than fernet
		- no need to install gnupg
	DISADVANTAGES:
		- just might not work if HandyApp's engineers didn't follow PKCKS
		padding fuidelines
		- slower than binary
	"""

	def __init__(self):
		with open("enc_params.config", mode="rt") as temp:
			x = temp.readlines()
		self.kbpdAlgo = 
		self.paddingAlgo = 
		return

	@classmethod
	def decrypt(self, filePath, fileBinary, key):
		""" filePath is ignored if fileBinary is available (?and usable)
		"""
		return decryptedBinary

	@classmethod
	def encrypt(self, filePath):
		""" function defined only for testing purposes i.e.
		can breaker decrypt a file it as encrypt using the same(or another) util.
		"""
		key = "0123"
		root, ext = os.path.splitext(filePath)
		outFile = root + ".enc" + ext
		return outFile




