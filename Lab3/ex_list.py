# List

# list vs variable
x = 100
print(x)
x = 100
print(x)

mylist = []
print(mylist)
print(type(mylist))

mylist = ['apple', 'banana', 'cherry']
# พิมพ์ข้อมูลที่อยู่ใน mylist
print(mylist)

# accessing list data
print(mylist[0]) #apple
print(mylist[1]) #apple
print(mylist[2]) #apple

# # accessing list data - negative index
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])

# accessing list data - range index
mylist = ['apple', 'banana', 'cherry', 'pineapple', 'orange']
print(len(mylist))

print(mylist[2:4])
print(mylist[2:5])
# พิมพ์ข้อมูลตำแหน่งที่ 1-3 ใน mylist
print(mylist[1:4])
# พิมพ์ข้อมูลตำแหน่งที่ 1 ถึงตำแหน่งสุดท้าย
print(mylist[1:])
# พิมพ์ข้อมูลตำแหน่งที่ 3 ถึงตำแหน่งุแรก
print(mylist[:4])

# accessing list data - loop
# for
print('Display with while loop:')
for x in mylist:
    print(x, type(x))
# while
print('Display with while loop:')
i = 0
while i < len(mylist):
    print(mylist[i], type(mylist[i]))
    i+=1

# changing data in list
mynum = [10,20,30,100,200,300]
print(mynum)
mynum[0] = 1000
print(mynum)
mynum[-1] = 3000
print(mynum)

# add data into list
mynum.append(4000)
print(mynum)

# insert data to list
# แทรกข้อมูล 500 ที่ตำแหน่งที่ 1 ของ mynum
mynum.insert(1,500)
print(mynum)

mynum[1:3] = [600,700]
print(mynum)

mynum[1:2] = [5,6]
print(mynum)

mynum[:5] = [10]
print(mynum)

# delete data in list
# remove()
mynum.remove(4000)
print(mynum)
# pop()
mynum.pop(0)
print(mynum)
mynum.pop()  # remove last object in list
print(mynum)
# key del
del mynum[1]  # delete index 1
print(mynum)
del mynum  # delete variable mynum
#print(mynum)

mynum = [1,2,3,4,5]
print(mynum)
mynum.clear()
print(mynum)


