"""
Name: [Phatchdawadee  Sariphat]
SID: [364211760035]
Group: [MIT212]
"""

myList = [10,20,30,40,50]

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# แสดงผลข้อมูล 20 จาก myList
print(myList[1])  # 20
# แสดงผลข้อมูล 50 จาก myList
print(myList[4])  # 50
# แสดงผลข้อมูล 50 จาก myList โดยใช้ negative index
print(myList[-1])  # 50
# แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[1:4])
# แสดงผลข้อมูล {40,50} โดยใช้ range index
print(myList[3:])
# แสดงผลข้อมูล {10,20} โดยใช้ range negative index
print(myList[:-3])
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ while loop
print('Display with while loop:')
i = 0
while i < len(myList):
    print(myList[i], type(myList[i]))
    i+=1
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ for loop
print('Display with while loop:')
for x in myList:
    print(x, type(x))
# เพิ่มข้อมูล 100,200,300 ใน myList
myList.append(100)
myList.append(200)
myList.append(300)
# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
myList.insert(0, 400)
# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
myList.insert(3, 500)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูล 10
myList.remove(10)
# ลบข้อมูล 100
myList.remove(100)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# เรียงข้อมูล myList จาก น้อย-มาก
myList.sort()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# เรียงข้อมูล myList จาก มาก-น้อย
myList.sort(reverse=True)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# comprehension
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
newlist = [x for x in myList if x > 50]
# แสดงผลข้อมูลใน newList ทั้งหมด
print(newlist)
# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
x = myList
y = newlist
myFinalList = x + y
# แสดงผลข้อมูลใน myFinalList ทั้งหมด
print(myFinalList)