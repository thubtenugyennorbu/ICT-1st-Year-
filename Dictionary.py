userdetails = {'Id' : 1, 'username': 'Just_me'}
print(type(userdetails))
print(userdetails)

location = dict(s = 'Samtse', t = 'Thimphu', p = 'Paro')
print(location)

print(userdetails['username'])
print(location['t'])
print(location.get('p'))

userdetails['email'] = 'justThubZ@example.com'
print(userdetails)

userdetails['username'] = 'Just_me_updated'
print(userdetails)

del location['p']
print(location)

deleted_value = userdetails.pop('email')
print(deleted_value)

del_key,del_value = userdetails.popitem()
print(f'the deleted key is {del_key} and the deleted value is {del_value}')

location.clear()
print(location)