import os
import time
import sys
def banner():
 os.system("apt install toilet")
 os.system("clear")
 os.system("toilet -fmono12 -F gay XPLOITS")
 print("    \033[1;36;40m Code made by: \033[1;32;40m anonymousmani")
 print("    \033[1;36;40m Inspired by : \033[1;32;40m tuhin bose")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/x_ploits")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/anonymousmani")
 print("    \033[1;31;40m    Use a VPN before running options [1] & [2].Otherwise it won't work")
 print("\n\n")
banner()
print("          \033[1;32;40m[1] \033[1;36;40mAnonymous Mail")
print("          \033[1;32;40m[2] \033[1;36;40mMail Bombing")
print("          \033[1;32;40m[3] \033[1;36;40mSms Bombing")
print("          \033[1;32;40m[4] \033[1;36;40mCall Bombing")
op=str(raw_input("\033[1;32;40mEnter>>>"))
if(op=='1'):
 os.system("python2 anonmail.py")
elif(op=='2'):
 os.system("python2 bombmail.py")
elif(op=='3'):
 os.system("python3 bomber.py")
elif(op=='4'):
 os.system("bash TBomb.sh")
else:
 print("\033[1;31;40mInvalid option.Quiting...")
 time.sleep(1.5)
 sys.exit()

 
 
