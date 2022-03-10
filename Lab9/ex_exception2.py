# Input Exception


# try:
#     num = int(input('Enter an integer: '))
#     print(f'The number that you entered is: {num}')
# except Exception as e:
#     print(e)

num = ''


def myfunc():
    global num
    num = input('Enter an integer: ') # str
    if not type(num) is int: # num is not integer
        raise TypeError('Only integer are allowed.',num)

try:
    myfunc()
except TypeError as e:
    print(e)

print(f'The number that you entered is: {num}')



