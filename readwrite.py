
#reads name.txt into a variable my_name and then
with open('name.txt') as f:
	my_name = f.read()

#writes a new file named hello.txt with the contents Hello, my name is <my_name>.
with open('hello.txt', 'w') as f:
	f.write("Hello, my name is " + my_name + "!")
