# set

myset = {'apple', 'banana', 'cherry'}
print(myset)
print(type(myset))
print(f'Lenght of myset is {len(myset)}')

# access data in set
# for
for x in myset:
    print(x)
# keyword in --> True, False
print('apple' in myset)  # True
print('Apple' in myset)  # False

myset2 = {10,1,20,True,100,'abc'}
print(myset2)

# add data to set
# add()
myset.add('mango')
print(myset)

# update()
myset3 = {'orang', 'grap'}
myset.update(myset3)
print(myset)

myset.add('mango')
print(myset)

mylist = ['pineapple', 'apple']
myset.update(mylist)
print(myset)

# dalete data in set
# remove()
myset.remove('apple')
print(myset)
myset.remove('pineapple')
print(myset)
# discard()
myset.discard('mango')
print(myset)

if 'apple' in myset:
    myset.discard('apple')
else:
    print('Set have no data apple')

print(myset)

# pop()
d = myset.pop()
print(d)
print(myset)
d = myset.pop()
print(d)
print(myset)
# keyword del
del myset3
print(myset)

