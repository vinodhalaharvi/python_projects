import os, sys, shlex
from subprocess import PIPE, STDOUT, Popen

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, ):
		super(ClassName, self).__init__()
		self.prefix = "dmctl -s TEST92-SA "
		
	def _run(self, *args, **kwargs):
		if self.prefix:
			cmd = self.prefix.split() + list(args)
		else:
			cmd = args
		proc = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
		return proc.communicate()


def run1(cmd_str):
	proc = Popen(shlex.split(cmd_str), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	return proc.communicate()

c = ClassName()
print list(c._run("getInstances", "ICIM_Notification"))
sys.exit(0)

for item in  c._run("getInstances", "ICIM_Notification"):
	if item:
		print item
sys.exit(0)




while True:
	print ">> ",
	line = raw_input()
	out, err = run(line)
	if out:
		print out
	if err:
		print err


