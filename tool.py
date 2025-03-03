# AUTHOR : MORTEZA ALIZADE
# GITHUB : MORTEZA-KING-007
# TELEGRAM CHANNEL : https://t.me/MortezaModz007
import os

if os.name == "nt":
	os.system("start https://t.me/MortezaModz007");
else:
	os.system("xdg-open https://t.me/MortezaModz007");

import sys
import time
import random
import datetime
import string
import platform
import subprocess
import base64
import shutil
import py_compile

try:
	import colorama
	import pyfiglet
except:
	os.system('pip install colorama pyfiglet')
	os.system('clear')
	import colorama
	import pyfiglet


from os import system
from sys import exit
from sys import stdout as std
from datetime import datetime
from platform import architecture
from pyfiglet import figlet_format
from colorama import Fore,Back
from sys import stdout as std
from time import sleep

RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
COOL = '\x1b[38;5;208m'

color = [YELLOW, GREEN, RED]


logo = f"""
{random.choice(color)}{figlet_format("[_ENCODE_]")}
\033[1;32m╔\033[1;32m𓆩M𓆪\033[1;32m══════════════════[\033[37;41m𓆩 𝐌𝐎𝐑𝐓𝐄𝐙𝐀 𓆪\033[0m\033[1;32m]════════════════\033[1;32m𓆩M𓆪\033[1;32m╗
\033[1;32m│\033[1;37m☞  \033[1;32mAUTHER     \033[1;37m➟   \033[1;32mMORTEZA ALIZADA                    \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mFACEBOOK   \033[1;37m➟   \033[1;32mMORTAZA ALIZADA                    \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mGITHUB    \033[1;37m ➟  \033[1;32m MORTEZA-KING-007                  \033[1;32m │
\033[1;32m│\033[1;37m☞  \033[1;32mVERSION   \033[1;37m ➟   \033[1;32m1.0                            \033[1;32m    │
\033[1;32m│\033[1;37m☞  \033[1;32mSTATUS    \033[1;37m ➟   \033[1;32mFREE                           \033[1;32m    │
\033[1;32m╚\033[1;32m𓆩M𓆪\033[1;32m═════\033[41m\033[1;37m[ 𓆩 𝐈𝐅 𝐘𝐎𝐔𝐑 𝐁𝐀𝐃,𝐒𝐎 𝐈 𝐀𝐌 𝐘𝐎𝐔𝐑 𝐃𝐀𝐃𓆪 ]\033[0m\033[1;32m═══════\033[1;32m𓆩M𓆪\033[1;32m╝
"""


def clear():
	system('clear')
	jan(f'\n{logo}', 0.00001)


def liner(int):
	print(int * f"{WHITE}=")


def bit():
	return architecture()[0]


class jan:
	def __init__(self, txt, t):
		for i in txt + '\n':
			std.write(i)
			std.flush()
			time.sleep(t)



def main():
	clear()
	liner(50)
	print(f'{WHITE}[✓] FULLY CODED WITH PYTHON  SUPPORT TERMUX')
	liner(40)
	print(f'{WHITE}[{YELLOW}01{WHITE}] ENCODE IMAGE')
	print(f'{WHITE}[{YELLOW}02{WHITE}] DECODE IMAGE')
	print(f'{WHITE}[{YELLOW}00{WHITE}]{RED} EXIT OPTION')
	liner(40)
	c = input(f'{GREEN}[✓] CHOOSE ANY OPTION -》')
	if c in ['01', '1']:
		enc_()
	elif c in ['02', '2']:
		dec_()
	elif c in ['00', '0']:
		clear()
		liner(50)
		sys.exit(f'{WHITE}\n\t\t[✓] VIP SCRIPT BY MORTEZA ALIZADA [✓]')
	else:
		main()



def enc_():
	clear()
	liner(50)
	liner(40)
	path = input(f"{WHITE}[✓] ENTER THE IMAGE PATH :-> ")
	file = f'{path}'
	
	clear()
	liner(50)
	std.write(f'\r{WHITE}[✓] ENCODING IMAGE ..|')
	time.sleep(1)
	std.write(f'\r{WHITE}[✓] ENCODING IMAGE ../')
	time.sleep(2)
	std.write(f'\r{WHITE}[✓] ENCODING IMAGE ..-\n')
	
	try:
		enc = base64.b64encode(open(file, 'rb').read()) #open file for encoding
	except Exception as e:
		exit(f'{RED}\n\t[×] FILE NOT FOUND TRY AGAIN [×]')
	n1 = file.lower()
	now = datetime.now()
	year = now.year
	month = now.month
	day = now.day
	name = 'IMG_'+f'{str(year)}-{str(month)}-{str(day)}.txt' # file name
	open(name, 'wb').write(enc)
	shutil.move(name, '/sdcard') # use shutil move() method to move file to sdcard
	liner(50)
	
	input(f'{WHITE}[✓] ENCODING DONE NOW ENJOY :-> '); main();



def dec_():
	clear()
	liner(50)
	liner(40)
	path = input(f"{WHITE}[✓] ENTER THE BASE64 ENCODED IMG PATH :-> ")
	file = f'{path}'
	
	clear()
	liner(50)
	std.write(f'\r{WHITE}[✓] DECODING IMAGE ..|')
	time.sleep(1)
	std.write(f'\r{WHITE}[✓] DECODING IMAGE ../')
	time.sleep(2)
	std.write(f'\r{WHITE}[✓] DECODING IMAGE ..-\n')
	
	try:
		enc = base64.b64decode(open(file, 'rb').read()) #open file for encoding
	except Exception as e:
		exit(f'{RED}\n\t[×] FILE NOT FOUND TRY AGAIN [×]')
	n1 = file.lower()
	now = datetime.now()
	year = now.year
	month = now.month
	day = now.day
	name = 'IMG_'+f'{str(year)}-{str(month)}-{str(day)}.webp' # file name
	open(name, 'wb').write(enc)
	shutil.move(name, '/sdcard') # use shutil move() method to move file to sdcard
	print(f'{WHITE}[✓] YOU CAN CHANGE THE FORMAT FROM WEBP')
	liner(50)
	
	input(f'{WHITE}[✓] ENCODING DONE NOW ENJOY :-> '); main();


if __name__ == '__main__':
	main()
