#automatically generated by the clientobjectgenerator
from clientproxy import *

class Barrier():
	def __init__(self, number):
		invoke_command(self, "__init__", number)

	def __str__(self):
		invoke_command(self, "__str__")

	def wait(self, args, _paxi_designated, _paxi_client_cmdno, _paxi_me):
		invoke_command(self, "wait", args, _paxi_designated, _paxi_client_cmdno, _paxi_me)

