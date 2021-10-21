# -*- coding: utf8 -*-
import os
if os.name=='nt':
	os.system('color')
def ascii(num,sep=6,end=''):
	args = [oct(num),num,hex(num)]
	char = repr(chr(num)).replace("'",'')
	return ''.join([str(i)+(sep-len(str(i)))*' ' for i in args])+char+(sep-len(char))*' '+end
l = ["Oct","Dec","Hex","Char",]
print(*l,sep='   ',end='')
print("   ",*l,sep='   ')

print('-'*50)
for i in range(64):
	print(ascii(i),ascii(i+64),sep='    ')