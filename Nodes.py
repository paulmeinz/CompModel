import numpy as np

#Activation nodes for computational model.

class node():
		def __init__ (self, inp = 0, inpc = -4, act = 0, out = 0, on = True, firing = False):
			
			self.inp = inp
			self.inpc = inpc
			self.act = act
			self.out = out
			self.on = on
			
		
		def Activate(self):
			
			if self.on:
				self.inp += np.random.normal(0,.25)
				self.inpc = self.inp*.01 + self.inpc * .99
				self.act = 1/(1 + np.exp(-1*self.inpc))
				

