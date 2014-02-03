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

class Memfibo(object):
	"""docstring for Memfibo"""
	def __init__(self, ):
		super(Memfibo, self).__init__()
		self.cache = {}

	def fibo(self, n):
		if n in self.cache: 
			return self.cache[n]
		else:
			result = 0 
			if n <= 2:
				return 1
			else:
				result =  self.fibo(n-1) + self.fibo(n-2)	
				self.cache[n] = result
				return result

if __name__ == '__main__':
	m = Memfibo()
	for index, i in enumerate(range(100)):
		print index, m.fibo(i)
