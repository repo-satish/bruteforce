"""
	the real brute-force breaker
	dependencies:
		oscrypto OR openSSL
"""

import os
import sys
import ctypes
import logging
import itertools
import subprocess

BOLO_TARARA = lambda key: ctypes.windll.user32.MessageBoxW(None,
		"\n\n\n\n\tThe password is:\t\t\t\n\n\t\t%s\n\n\n\n" % (key),
		"\tPASSWORD CRACKED !", 0
	)

class init:
	
	crypto = None

	@classmethod
	def libraryAvailable(self):
		try:
			import oscrypto
		except ImportError:
			return False
		return True

	@classmethod
	def binaryAvailable(self):
		try:
			if subprocess.run("openssl ", stdout=subprocess.DEVNULL, \
			stderr=subprocess.DEVNULL).returncode == 0:
				return True
		except FileNotFoundError:
			choice = input("Would you like to specifiy custom path to openssl binary (y/n)?")
			if choice[0] in "yY":
				return True if BinaryCrypto.setBinPath() else False

	@classmethod
	def init(self):
		if self.libraryAvailable():
			self.crypto = "crypto_lib"
		elif self.binaryAvailable():
			self.crypto = "crypto_bin"
		else:
			logging.critical("no trustworthy decryption utility is available")
			sys.exit(1)
		return self




class breaker:

	size = 3
	crypto = None
	challenges = None	# [[filePath][bin], [filePath][bin], [filePath][bin]]

	# @classmethod
	# def __init__(self):
	# 	findChallenge(??)
	# 	return self

	@classmethod
	def init(self, importedLib):
		self.crypto = importedLib
		return

	@classmethod
	def findChallenge(self, dirPath):
		dirPath = os.path.abspath(dirPath)
		for r, d, f in os.walk(dirPath):
			break
		f = [os.path.join(r, _) for _ in f]
		files = sorted(f, key=lambda aFile: os.stat(aFile).st_size)[0:3]
		bins = list()
		for _ in files:
			with open(_, mode="rb") as temp:
				bins.append(temp.read())
		self.challenges = list(zip(files, bins))
		return
		# see weakref ?		# if len(d) > 0:	sys.exit("inappropriate, dirPath contains folders")		# if not set([os.path.splitext(_)[1] for _ in f]).issubset(set(['png', 'jpg', 'jpeg'])):

	@classmethod
	def tryCrack(self, key):
		_tryCrack = lambda p_bPair, guess: self.crypto.decrypt(
			filePath=p_bPair[0],
			fileBinary=p_bPair[1],
			key=guess
		)
		expectedFormat = set(['png', 'jpeg'])
		decryptedBinary = _tryCrack(self.challenges[0], key)
		if imghdr.what(None, h=decryptedBinary) in expectedFormat:
			a = _tryCrack(self.challenges[1], key)
			b = _tryCrack(self.challenges[2], key)
			x, y = imghdr.what(None, h=a), imghdr.what(None, h=b)
			if set([x, y]).issubset(expectedFormat):
				BOLO_TARARA(key)
				sys.exit(0)
		else:
			return

	@classmethod
	def passwordGen(self, pool, size):
		for aPassword in itertools.permutations(pool, size):
			pwd = "".join(aPassword)
			yield pwd

	@classmethod
	def brute_force(self):
		print("Beginning cracking with password length %d" % self.size)
		password = self.passwordGen("0123456789", self.size)
		while True:
			try:
				key = next(password)
			except StopIteration:
				ch = input("Increase password length, currently %d [Y/n]?\n" % self.size)
				if ch=='n':	sys.exit("You quit!")
				self.size+= 1
				brute_force()
			self.tryCrack(key)
		return




if __name__ == '__main__':
	breaker.init(
		__import__(init.init().crypto)
	)
	breaker.brute_force()