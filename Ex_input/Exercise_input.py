# Exercise input()

"""
1.เขียนโปรแกรมรับค่าตัวเลขจำนวนเต็ม 3 จำนวน
"""
# x,y,z = [int(x) for x in input('Enter 3 values: ').split()]
# print(f'Summation is {x+y+z}')
"""
2.
"""
# mynum = [int(x) for x in input('Enter multi values: ').split()]
# total = 0
# for x in mynum:
    # total+=x
# print(f'Summation of in list is {total}')
"""
3.
"""
myEven = [int(x) for x in input("enter multi integers: ").split()
          if int(x)%2 ==0]
print(f'Even num in myEven list: {myEven}')
