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



def _run(cmd, domains):
	if 'brcontrol' in cmd:
		os.system(cmd)
		return 

	if 'attach' == cmd.split()[0]:
		domains += cmd.split()[1:]
		print "Attached domains: ", domains
		return 

	if not domains:
		print "Not domains attached .." 
		print "Attach a domain first using 'attach' command"
	
	
	for domain in domains:
		prefix = "dmctl -s %s " % domain
		suffix = " | tee"
		command = prefix + cmd  + suffix
		prefix  = ""
		if len(domains) > 1:
			print 
			print domain + '::' + command
		os.system(command)
		command = ""


class Completer(object):
	def __init__(self):
		"""docstring for __init__"""
		self.prefix = "dmctl -s "

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
		if len(args) == 1:
			return [c + ' ' for c in CLASSES if args[0] in c]
		else:
			return ["clear <class::instance::event>", '']
        

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
		else:
			return ["Usage: findInstances <class-regexp>::<instance-regexp>", "",]


        def complete_get(self, args):
                """docstring for get"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
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
		else:
			return ["Usage: getEvents [<class>]", '']
        

        def complete_getEventDescription(self, args):
                """docstring for getEventDescription"""
                return ["Not Supported Yet", ""]
        

        def complete_getInstances(self, args):
                """docstring for getInstances"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
		else:
			return ["Usage: getInstances [<class>]", '']

        def complete_getModels(self, args):
                """docstring for getModels"""
		return ['Usage: getModels', '']

        def complete_getOperations(self, args):
                """docstring for getOperations"""
                if len(args) == 1:
                        return [c + ' ' for c in CLASSES if args[0] in c]
		else:
			return ['Usage: getOperations <class>', '']
        

        def complete_getPrograms(self, args):
                """docstring for getPrograms"""
		return ['Usage: getPrograms', '']
        

        def complete_getProperties(self, args):
                """docstring for getProperties"""
                return ["Not Supported Yet", ""]
        

        def complete_getThreads(self, args):
                """docstring for getThreads"""
                return ["getThreads", ""]
        

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
		if len(args) == 1:
			return [c + ' ' for c in CLASSES if args[0] in c]
		else:
			return ["clear <class::instance::event>", '']

        def complete_ping(self, args):
                """docstring for ping"""
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
		return ['status', '']
        

        def complete_save(self, args):
                """docstring for save"""
		if len(args) == 1:
			return ["save <file> [<class>]", '']
		elif len(args) == 2:
			return [c + ' ' for c in CLASSES if args[-1] in c]
		else:
			return ["save <file> [<class>]", '']
        

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

if __name__ == '__main__':
	comp = Completer()
	exclude_list = ("", )
	readline.set_completer_delims(' \t\n;')
	readline.parse_and_bind("tab: complete")
	readline.parse_and_bind("enter: complete")
	readline.parse_and_bind('set editing-mode vi')
	readline.set_completer(comp.complete)
	domains = ['TEST92-SA',]
	while True:
		line = raw_input('>> ')
		if line:
			cmd = line.split()[0]
		else:
			continue
		if cmd == 'attach':
			domains += line.split()[1:]
			print domains
			continue
		if cmd == 'detach':
			domains  = [d for d in domains if d != line.split()[-1]]
			print domains
			continue
		if cmd and (cmd not in COMMANDS or cmd in exclude_list):
			os.system(line)
		else:
			_run(line, domains)

