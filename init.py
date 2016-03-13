"""
	initializer
		stores important data required to properly run this app
"""

import sys
import logging
import warnings
import importlib
import subprocess

def init():
	try:
		getattr(importlib, "import_module")("oscrypto")
	except ImportError:
		warnings.warn("Critical decryption library `oscrypto` is not installed . . .")
		x = subprocess.run(["openssl"], shell=True)
		if x.returncode == 0:
			import decBin as crypto # decryptor = "bin"	# switch decryptor to openssl
		else:
			if input("Would you like to specifiy custom path to openssl binary (y/n)?")[0] in "yY":
				import decBin
				decBin.setBinPath()
			else:
				logging.critical("no trustworthy decryption utility is available")
				sys.exit(1)
	import decLib as crypto
