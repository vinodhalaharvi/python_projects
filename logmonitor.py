###########################
# Author: Vinod Halaharvi
# Email: vinod.halaharvi@gmail.com
###########################

import time
import fcntl
import os
import signal
from optparse import OptionParser
import sys
import optparse

class LogMonitor(object):
        """docstring for LogMonitor"""
        def __init__(self, dirname):
                super(LogMonitor, self).__init__()
                self.dirname = dirname
                self.modified = False
                #FNAME = "/tmp/testdir"

        def _handler(self, ignore, ig):
                """docstring for _handler"""
                self.modified = True

        def setup(self, signum, frame):
                signal.signal(signal.SIGIO, self._handler)
                fd = os.open(self.dirname,  os.O_RDONLY)
                fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
                fcntl.fcntl(fd, fcntl.F_NOTIFY,
                            fcntl.DN_MODIFY | fcntl.DN_CREATE | fcntl.DN_MULTISHOT)

        def watch(self):
                """docstring for watch"""
                while True:
                        print self.modified
                        if self.modified:
                                self.modified = False
                                print "File %s modified" % (self.dirname,)
                        time.sleep(1)
        
        def sendmail(self):
                """docstring for sendmail"""
                pass

def get_options():
        """docstring for optparse"""
        parser = OptionParser()
        parser.add_option("-d", "--dir", dest="dirname",
                          help="Directory to watch", metavar="FILE")
        parser.add_option("-d", "--email", dest="email_address",
                          help="Email address")
        parser.add_option("-q", "--quiet",
                          action="store_false", dest="verbose", default=True,
                          help="don't print status messages to stdout")
        (options, args) = parser.parse_args()
        return options


if __name__ == '__main__':
        options = get_options()
        lm = LogMonitor(options.dirname)
        lm.setup(0, 0)
        lm.watch()
