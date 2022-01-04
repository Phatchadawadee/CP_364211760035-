# Globle variable

x = 'MIT'
print(x)


def myfunc():
      # local varoable
      x = 'RUTS'
      print(x)

def myfunc2():
      global x
      x = 'Saiyai'
      print(x)

# call myfunc()
myfunc2()
print(x)
