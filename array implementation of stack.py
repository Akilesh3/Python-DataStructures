class Stack:

	def __init__(self):
		self.stack = []

	def add(self,dataval):
		if dataval not in self.stack:
			self.stack.append(dataval)
		else:
			return False
	def remove(self):
		if self.stack == None:
			return ("The stack is empty")
		else:
			return self.stack.pop()	

	def peek(self):	
		return self.stack[-1]	

stk = Stack()
stk.add("mon")
stk.add("tue")			
stk.add("thu")		
print(stk.remove())
stk.add("fri")
print(stk.peek())