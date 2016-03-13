"""
	PUORPOSE:
	to check that the brute-force machine with all its components is actually
	working - i.e. when the algorithms used for padding, key derivation and
	encryption are known CORRECTLY
"""

from raw import img
from breaker import breaker, init

import os
import base64
import tempfile

def createTestImages():
	for _ in img.keys():
		with open(_, mode="wb") as temp:
			temp.write(    base64.b64decode(img[_])    )
	print("Test images written successfully")
	return True

def encryptTestImages(simpleKey):
	return True	

def calcSHA1(filePath):
	import hashlib
	hashVal = hashlib.sha1()
	with open(filePath, mode="rb") as temp:
		while True:
			x = temp.read(2 * 1024)
			if len(x)==0:	break
			hashVal.update(x)
	ans = hashVal.hexdigest()
	return ans[:6] + "..." + ans[-3:]

def main():
	init()

	if createTestImages():
		encryptTestImages("0123")

	breaker.findChallenge(  os.getcwd()  )
	breaker.brute_force()

	return
