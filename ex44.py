class Parent(object):
	def implicit(self):
		print "PARENT implicit()"

	def override(self):
		print "PARENT override()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print

dad.override()
son.override()

print

dad.altered()
son.altered()





'''
N = int(raw_input('Enter a number: '))

for i in range(0, N):
	for j in range(N, i, -1):
		print ' ',

	print ' /',

	for k in range(0, i + 1):
		print ' * ',

	print '\\',

	print ''
	'''

