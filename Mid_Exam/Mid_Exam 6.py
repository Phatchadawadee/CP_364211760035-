"""
Name: {Phatchadawadee  Sariphat}
SID: {364211760035}
Group: {MIT212}
"""

"""
Question 6:
จงเขียนโปรแกรมรับค่าปี ค.ศ. จากนั้นให้แสดงผลปี พ.ศ.
และผลรวมของตัวเลขแต่ละหลักของปี ค.ศ. และ พ.ศ. ดังตัวอย่างต่อไปนี้

Input (ค.ศ.): 2022
Output (พ.ศ.): 2565
Sum (ค.ศ.): 6
Sum (พ.ศ.): 18


(10 คะแนน)
"""
try:
    year = int(input( 'Input (ค.ศ.):' ))
except:
    year = 0

if year > 0:
    x = year + 543
    print('Output (พ.ศ.):',x,)
try:
    year = int(input( 'sum (ค.ศ.):' ))
except:
    year = 0

if year > 0:
    x = year + 12
    print('sum (พ.ศ.):',x,)
