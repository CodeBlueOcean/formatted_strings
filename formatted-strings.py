# formatted strings

name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' year old')

'Andrei'
'Joe'

# formatted strings

name = 'Johnny'
age = 55

print(f'hi {name}. You are {age} years old')

'Andrei'
'Joe'

# formatted strings another ex

name = 'Johnny'
age = 55

print('hi {}. You are {} years old'.format('Johnny','55'))

'Andrei'
'Joe'

# formatted strings another ex

name = 'Johnny'
age = 55

print('hi {1}. You are {0} years old'.format(name, age))

'Andrei'
'Joe'

# formatted strings another ex

name = 'Johnny'
age = 55

print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))

'Andrei'
'Joe'

# formatted strings another ex

name = 'Johnny'
age = 55

print(f'hi {name}. You are {age} years old')

'Andrei'
'Joe'


