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

def sendemail(subject, msg):
        import smtplib, getpass, sys
        gmail_user = "vinod.halaharvi@gmail.com"
        gmail_pwd = 'bkabovsodltmldpb'
        FROM = 'vinod.halaharvi@gmail.com'
        TO = ['vinod.halaharvi@gmail.com'] 
        SUBJECT = subject
        TEXT = msg

        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
                server = smtplib.SMTP("smtp.gmail.com", 587) 
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                server.close()
                print 'successfully sent the mail'
        except:
                raise
                print "failed to send mail"


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
                        #print self.modified
                        if self.modified:
                                self.modified = False
                                sendemail("ALERT: DIR %s modified" % (self.dirname,), "DIR MODIFIED") 
                                print "Email sent"
                                print "File %s modified" % (self.dirname,)
                        time.sleep(10)
        
        def sendmail(self):
                """docstring for sendmail"""
                pass

def get_options():
        """docstring for optparse"""
        parser = OptionParser()
        parser.add_option("-d", "--dir", dest="dirname",
                          help="Directory to watch", metavar="FILE")
        parser.add_option("-e", "--email", dest="email_address",
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
