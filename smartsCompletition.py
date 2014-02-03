# Copyright (c) 2013, RTP Network Services, Inc.
# All Rights Reserved      (904-236-6993)
# Vinod Halaharvi / vinod.halaharvi@rtpnet.net, vinod.halaharvi@gmail.com
# 
# http://www.rtpnet.net / codesupport@rtpnet.net
#
# There is NO warranty for this software.  If this software is used by
# someone else and passed on, the recipients should know that what they
# have is not the original, so that any problems introduced by others will
# not reflect on the original authors' reputations. This is *not* authorization
# to copy or distribute this software to others!

import os
import re
import readline
from smartslib import CLASSES
import os, sys, shlex
from subprocess import PIPE, STDOUT, Popen
import time
#COMMANDS = ['extra', 'extension', 'stuff', 'errors',
#                  'email', 'foobar', 'foo']

COMMANDS = ( "attach", "clear", "create", "consistencyUpdate", "correlate", "delete", "detach", "execute", "findInstances", "get", "getClasses", "getEvents", "getEventDescription", "getInstances", "getModels", "getOperations", "getPrograms", "getProperties", "getThreads", "insert", "invoke", "loadModel", "loadProgram", "notify", "ping", "put", "quit", "remove", "restore", "shutdown", "status", "save", "brcontrol", )


RE_SPACE = re.compile('.*\s+$', re.M)

def _run(cmd):
	os.system(cmd)
	return
	proc = Popen(shlex.split(cmd), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	return proc.communicate()


class Completer(object):
	def __init__(self):
		"""docstring for __init__"""
		self.prefix = "dmctl -s TEST92-SA "

        def _listdir(self, root):
            "List directory 'root' appending the path separator to subdirs."
            res = []
            for name in os.listdir(root):
                   path = os.path.join(root, name)
                   if os.path.isdir(path):
                          name += os.sep
                   res.append(name)
            return res


        def _run(self, *args, **kwargs):
		if self.prefix:
			cmd = self.prefix.split() + list(args)
		else:
			cmd = args
		print 
		print cmd
		if 'brcontrol' in cmd:
			proc = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
			return proc.communicate()
		else:
			proc = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
			return proc.communicate()
	#return ["test" + ' ']

        def _complete_path(self, path=None):
            "Perform completion of filesystem path."
            if not path:
                   return self._listdir('.')
            dirname, rest = os.path.split(path)
            tmp = dirname if dirname else '.'
            res = [os.path.join(dirname, p)
                          for p in self._listdir(tmp) if p.startswith(rest)]
            # more than one match, or single match which does not exist (typo)
            if len(res) > 1 or not os.path.exists(path):
                   return res
            # resolved to a single directory, so return list of files below it
            if os.path.isdir(path):
                   return [os.path.join(path, p) for p in self._listdir(path)]
            # exact file match terminates this completion
            return [path + ' ']


    	def complete_brcontrol(self, args):
                """docstring for complete_brcontrol"""
                if len(args) == 1:
			for item in self._run('brcontrol'):
				if item:
					print item
		else:
			return ['brcontrol', '']


        def complete_attach(self, args):
                """docstring for attach"""
                return ["Not Supported Yet", ""]
        

        def complete_clear(self, args):
                """docstring for clear"""
                return ["Not Supported Yet", ""]
        

        def complete_create(self, args):
                """docstring for create"""
                return ["Not Supported Yet", ""]
        

        def complete_consistencyUpdate(self, args):
                """docstring for consistencyUpdate"""
                return ["Not Supported Yet", ""]
        

        def complete_correlate(self, args):
                """docstring for correlate"""
                return ["Not Supported Yet", ""]
        

        def complete_delete(self, args):
                """docstring for delete"""
                return ["Not Supported Yet", ""]
        

        def complete_detach(self, args):
                """docstring for detach"""
                return ["Not Supported Yet", ""]
        

        def complete_execute(self, args):
                """docstring for execute"""
                return ["Not Supported Yet", ""]
        

        def complete_findInstances(self, args):
                """docstring for findInstances"""
		if len(args) == 1:
			return [c + ' ' for c in CLASSES if args[0] in c]
		elif len(args) == 2:
			cls_reg, inst_reg = args
			for item in self._run("findInstances", "%s::.*%s.*" % (cls_reg, inst_reg)):
				if item:
					print item
		else:
			return ["Usage: findInstances <class-regexp>::<instance-regexp>", "",]


        def complete_get(self, args):
                """docstring for get"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
		elif len(args) == 2:
			cls, inst  = args
			for item in self._run("get", "%s::%s" % (cls, inst)):
				if item:
					print item
		elif len(args) == 3:
			cls, inst, prop  = args
			for item in self._run("get", "%s::%s::%s" % (cls, inst, prop)):
				if item:
					print item
		else:
			return ['Usage: get <class> <instance> [<property>]', '']

        def complete_getClasses(self, args):
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
		else:
			return ['getClasses', '']


        def complete_getEvents(self, args):
                """docstring for getEvents"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
                elif len(args) == 2:
			_class = args[0].strip()
			for item in self._run("getEvents", _class):
				if item:
					print item
		else:
			return ["Usage: getEvents [<class>]", '']
        

        def complete_getEventDescription(self, args):
                """docstring for getEventDescription"""
                return ["Not Supported Yet", ""]
        

        def complete_getInstances(self, args):
                """docstring for getInstances"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
                elif len(args) == 2:
			_class = args[0].strip()
			for item in self._run("getInstances", _class):
				if item:
					print item
		else:
			return ["Usage: getInstances [<class>]", '']

        def complete_getModels(self, args):
                """docstring for getModels"""
                if len(args) == 1:
			for item in  self._run('getModels'):
				if item:
					print item
		else:
			return ['Usage: getModels', '']

        def complete_getOperations(self, args):
                """docstring for getOperations"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
		elif len(args) == 2:
			_class = args[0].strip()
			for item in self._run("getOperations", _class):
				if item:
					print item
		else:
			return ['Usage: getOperations <class>', '']
        

        def complete_getPrograms(self, args):
                """docstring for getPrograms"""
                if len(args) == 1:
			for item in  self._run('getPrograms'):
				if item:
					print item
		else:
			return ['Usage: getPrograms', '']
        

        def complete_getProperties(self, args):
                """docstring for getProperties"""
                return ["Not Supported Yet", ""]
        

        def complete_getThreads(self, args):
                """docstring for getThreads"""
                return ["Not Supported Yet", ""]
        

        def complete_insert(self, args):
                """docstring for insert"""
                return ["Not Supported Yet", ""]
        

        def complete_invoke(self, args):
                """docstring for invoke"""
                return ["Not Supported Yet", ""]
        

        def complete_loadModel(self, args):
                """docstring for loadModel"""
                return ["Not Supported Yet", ""]
        

        def complete_loadProgram(self, args):
                """docstring for loadProgram"""
                return ["Not Supported Yet", ""]
        

        def complete_notify(self, args):
                """docstring for notify"""
                return ["Not Supported Yet", ""]
        

        def complete_ping(self, args):
                """docstring for ping"""
		if len(args) == 1:
			for item in  self._run('ping'):
				if item:
					print item
		else:
			return ['Usage: ping', '']
        

        def complete_put(self, args):
                """docstring for put"""
                return ["Not Supported Yet", ""]
        

        def complete_quit(self, args):
                """docstring for quit"""
                return ["Not Supported Yet", ""]
        

        def complete_remove(self, args):
                """docstring for remove"""
                return ["Not Supported Yet", ""]
        

        def complete_restore(self, args):
                """docstring for restore"""
                return ["Not Supported Yet", ""]
        

        def complete_shutdown(self, args):
                """docstring for shutdown"""
                return ["Not Supported Yet", ""]
        

        def complete_status(self, args):
                """docstring for status"""
                if len(args) == 1:
			for item in  self._run('status'):
				if item:
					print item
		else:
			return ['status', '']
        

        def complete_save(self, args):
                """docstring for save"""
                return ["Not Supported Yet", ""]
        

        def complete_extra(self, args):
            "Completions for the 'extra' command."
            if not args:
                   return self._complete_path('.')
            # treat the last arg as a path and complete it
            return self._complete_path(args[-1])

        def complete(self, text, state):
            "Generic readline completion entry point."
            buffer = readline.get_line_buffer()
            line = readline.get_line_buffer().split()
            # show all commands
            if not line:
                   return [c + ' ' for c in COMMANDS][state]
            # account for last argument ending in a space
            if RE_SPACE.match(buffer):
                   line.append('')
            # resolve command to the implementation function
            cmd = line[0].strip()
            if cmd in COMMANDS:
                   impl = getattr(self, 'complete_%s' % cmd)
                   args = line[1:]
                   if args:
                          return (impl(args) + [None])[state]
                   return [cmd + ' '][state]
            results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
            return results[state]

comp = Completer()
# we want to treat '/' as part of a word, so override the delimiters
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.parse_and_bind('set editing-mode vi')
#readline.read_history_file()
#readline.write_history_file()
#readline.set_history_length(1000)
readline.set_completer(comp.complete)
while True:
	line = raw_input('>> ')
	if line and  line not in COMMANDS:
		os.system(line)
		continue
