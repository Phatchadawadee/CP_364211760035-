"""
Name: {Phatchadawadee  Sariphat}
ID: {364211760035}
Group: {MIT212}
"""
"""
Question 2:
จงเขียนโปรแกรมหาตัวเลขที่เลข 3 หรือ 5 หรือ 7 หารลงตัว จากเลข 1 ถึงตัวเลขที่ป้อนทางคีย์บอร์ด โดยแสดงตัวเลขว่ามีกี่จำนวน ต่อด้วยตัวเลขที่หารลงตัวโดยแต่ละตัวคั่นด้วยเว้นวรรค  และเขียนผลลัพท์ที่ได้ลงในไฟล์ชื่อ final1.txt  เช่น
Enter number: 20
The result is 8: 3 5 9 10 12 15 18 20
(5 คะแนน)
"""
f = open("final1.txt", 'a')
i = int(input("Enter number: "))
count = 0
while count <= i:
    if i % 3 == 0:
        print(f'The result is : ', count)
        count = count+5