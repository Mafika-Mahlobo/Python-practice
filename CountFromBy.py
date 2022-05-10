class CountFromBy:
	def __init__(self, v: int = 0, i: int = 1) ->None:
		self.value = v
		self.incr = i

	def __repr__(self):
		return str(self.value)

	def increase(self):
		self.value += self.incr

a = CountFromBy()
for i in range(3):
	a.increase()

b = CountFromBy(i=5)

b.increase()
print(b.value)
