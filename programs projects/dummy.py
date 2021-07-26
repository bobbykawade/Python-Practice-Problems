#decorators
#class method
#static method
class Dummy:
	c = 0
	def assign_name(self, n):
		self.name = n

		@classmethod  #decorator
		def class_method_test(cls):
			cls.c += 1
			print('inside class method')

			@staticmethod
			def display(a):
				print(a)

				a = Dummy()
				a.assign_name('manas')
				print(a.name)
				Dummy().class_method_test()
				print(Dummy.c)
				Dummy().display('abc')



				#pep 8 
				no_of_students

				#docstring
				def test:
