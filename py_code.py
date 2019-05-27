from ctypes import *

libc_ode = CDLL("./libc_ode.so")

assert libc_ode.c_add(2, 2) == 4
libc_ode.c_print()

mylist = ['\x41', '\x42', '\x43']
byte_array = (c_byte * 4)()

for i in range(len(mylist)):
    #byte_array[i] = int((mylist[i]).encode('hex'), 16)
    byte_array[i] = ord(mylist[i])
cast(byte_array, POINTER(c_byte))

c_bytes_func = libc_ode.c_bytes
c_bytes_func.restype = c_char_p
pointer = libc_ode.c_bytes(byte_array, 3)

print pointer
