"""
Name: {Phatchadawadee  Sariphat}
ID: {364211760035}
Group: {MIT212}
"""
"""
Quesiton 6:
เขียนโปรแกรมเพื่อนับสระในภาษาอังกฤษ (Vowels: a e i o u) 
โดยรับข้อความจากผู้ใช้ จากนั้นให้โปรแกรมแสดงผลว่าจากข้อความดังกล่าว
มีสระแต่ละตัวมีจำนวนเท่าไร

Example:

Input message:  The National Vaccine Board approved a 
policy with the additional target of procuring 150 million 
doses of COVID-19 vaccines by 2022

Result:
a = 10
e = 7
I = 11
o = 11
u = 1 

"""
while(True):
    phrase = input('Input message: ')
    if phrase == 'and':
        quit()
    lower = str.lower(phrase)
    convert = list(lower)
    a = convert.count('a')
    e = convert.count('e')
    i = convert.count('i')
    o = convert.count('o')
    u = convert.count('u')

    vowel = a + e + i + o + u
    break
print ('\n')
print ('a = ', a)
print ('e = ', e)
print ('i = ', i)
print ('o = ', o)
print ('u = ', u)