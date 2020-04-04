import requests
import os

def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F border X_PLOITS")
 print("    \033[1;36;40m TOOL        : \033[1;32;40m Send Anonymous Mails To Your Victim ")
 print("    \033[1;36;40m Code made by: \033[1;32;40m anonymousmani")
 print("    \033[1;36;40m Inspired by : \033[1;32;40m tuhin bose")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/x_ploits")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/anonymousmani")
 print("    \033[1;31;40m    Use a VPN before running it.Otherwise it won't work")
 print("\n\n")
banner()
userid = str(raw_input("\033[1;33;40mEnter The Email-id of victim : "))
subject = str(raw_input("\n\033[1;33;40mEnter the subject of your email : "))
message = str(raw_input("\n\033[1;33;40mEnter the message : "))
with requests.session() as s:
 data1={'to':userid,'subject':subject,'text':message}
 r=s.post('http://anonymouse.org/cgi-bin/anon-email.cgi',data=data1)
 if('The e-mail has been sent anonymously!' in r.text):
  print("\n\033[1;32;40mSuccess.To protect your privacy, E-mail will be sent within 12 hours\n")
 else:
  print("\n\033[1;31;40mE-mail can't be sent. Try again.\n")
   
