# Berikut ini cara membuka dan membaca dari sebuah file.

>>> f = open('workfile','rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)
5
>>> f.read(1)
b'5'
>>> f.seek(-3,2)
13
>>> f.read(1)
b'd'
