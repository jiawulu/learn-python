msg = ''' ------- {name} ---------
{name}
{age}
{gender}
'''

print(msg)

print(msg.format(name='Hodor', age='Hodor!', gender='gender'))


msg2 = ''' -------  ---------
{}
{}
{}
'''
print(msg2.format('a','b','c'))