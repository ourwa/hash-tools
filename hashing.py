import hashlib
import colorama
from hashlib import * 
colorama.init(autoreset=True)
style = '''\033[31m
.-. .-.  .--.   .----..-. .-.    .---.  .----.  .----. .-.    .----.
| {_} | / {} \ { {__  | {_} |   {_   _}/  {}  \/  {}  \| |   { {__  
| { } |/  /\  \.-._} }| { } |     | |  \      /\      /| `--..-._} }
`-' `-'`-'  `-'`----' `-' `-'     `-'   `----'  `----' `----'`----'  \033[33m by ourwa
'''
print(style)
print("\033[36m==========================================================")
print("\033[35m[1]hashing chacker\n[2]length hash\n[3]hashing type\n[4]md5 encrepting\n[5]md5 decrept\033[38m")
print("\033[36m==========================================================")

choose= input("please choose option:")
if choose== '1':
	print("hashing chacker")
	hash1=input("enter hash[1]")
	hash2=input("enter hash[2]")
	if hash1==hash2:
		print("your hash is clear")
	else:
		print("your hash is virus")
if choose=='2':
	print("####length hash####")
	length=input("enter your hash for calcolet:")
	print("length hash is:",len(length))
if choose=='3':
	print("hashing type")
	hash=input("enter your hash:")
	length=len(hash)
	if length==32:
		print("the hash is [md5]")
	if length==40:
		print("the hash is [sha1]")
	if length==64:
		print("the hash is [sh264]")
if choose=='4':
	print("this option for encrepting by md5")
	word = input("enter your words :")
	md5  = hashlib.md5(word.encode())
	print(md5.hexdigest())
if choose=='5':
	print("this option for decrepting")
	hash= input("enter your hash :")
	file= input("write file name :")
	with open (file , mode='r')as f:
		for line in f :
			line = line.strip()
			if md5(line.encode()).hexdigest() == hash :
				print ("[-] Password Found :" +line)
			
		

	
